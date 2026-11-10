"""Apply a transparent example review-priority matrix to exposure facts."""

from runtime import choice, cli, report, rows, strings, text, unique


def analyze(data):
    threat_id = text(data.get("threat_id"), "threat_id")
    exploitation = choice(
        data.get("exploitation"), ["active", "not_reported", "unknown"], "exploitation"
    )
    assets = rows(data.get("assets"), "assets")
    unique(assets)
    findings = []
    for asset in assets:
        affected = choice(
            asset.get("affected"), ["yes", "no", "unknown"], "asset.affected"
        )
        exposure = choice(
            asset.get("exposure"), ["internet", "internal", "unknown"], "asset.exposure"
        )
        criticality = choice(
            asset.get("criticality"),
            ["high", "standard", "unknown"],
            "asset.criticality",
        )
        refs = strings(asset.get("evidence_ids"), "asset.evidence_ids")
        if affected in ("yes", "no") and not refs:
            raise ValueError("a known affected state requires evidence_ids")
        if affected == "no":
            priority, reason = (
                "verify_non_applicability",
                "Caller reports this asset is not affected.",
            )
        elif affected == "unknown":
            priority, reason = "investigate_exposure", "Affected status is unresolved."
        elif exploitation == "active":
            priority, reason = (
                "urgent_review",
                "Confirmed affected asset and reported active exploitation.",
            )
        elif "unknown" in (exposure, criticality, exploitation):
            priority, reason = (
                "resolve_missing_facts",
                "Affected asset has unresolved prioritization facts.",
            )
        elif exposure == "internet" and criticality == "high":
            priority, reason = (
                "urgent_review",
                "Affected, internet-exposed asset with high business criticality.",
            )
        elif exposure == "internet" or criticality == "high":
            priority, reason = (
                "expedited_review",
                "Affected asset is internet exposed or has high criticality.",
            )
        else:
            priority, reason = (
                "scheduled_review",
                "Affected internal asset with standard criticality; exploitation not reported.",
            )
        findings.append(
            {
                "asset_id": asset["id"],
                "priority": priority,
                "reason": reason,
                "affected": affected,
                "exposure": exposure,
                "criticality": criticality,
                "evidence_ids": refs,
            }
        )
    return report(
        "Threat Prioritization Agent",
        {
            "threat_id": threat_id,
            "assets": len(assets),
            "exploitation": exploitation,
            "policy": "example-matrix-v1",
        },
        findings,
        [
            "This is an original illustrative matrix, not CERT/CC SSVC, CVSS or an organizational severity policy.",
            "Input evidence references are preserved but are not retrieved or independently authenticated.",
            "Not reported does not establish that exploitation is absent. Unknown facts never become a low-risk assumption.",
            "Priorities carry no automatic patch deadline. Controls, business impact and policy-specific obligations need review.",
        ],
        [
            "Validate exposure, exploitation and business-criticality facts with dated evidence.",
            "Have the asset owner assign a remediation target under the applicable policy.",
            "Reassess when exploitation, exposure, evidence quality or control effectiveness changes.",
        ],
    )


if __name__ == "__main__":
    cli(analyze, __doc__)
