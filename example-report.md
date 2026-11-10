# Threat Prioritization Agent

## Summary

- **threat id:** DEMO-2026-001
- **assets:** 3
- **exploitation:** not\_reported
- **policy:** example-matrix-v1

## Findings

### Finding 1

- **asset id:** lab-gateway
- **priority:** urgent\_review
- **reason:** Affected, internet-exposed asset with high business criticality\.
- **affected:** yes
- **exposure:** internet
- **criticality:** high
- **evidence ids:** \["demo-inventory-1", "demo-advisory-1"\]

### Finding 2

- **asset id:** lab-worker
- **priority:** investigate\_exposure
- **reason:** Affected status is unresolved\.
- **affected:** unknown
- **exposure:** internal
- **criticality:** standard
- **evidence ids:** \[\]

### Finding 3

- **asset id:** lab-service
- **priority:** scheduled\_review
- **reason:** Affected internal asset with standard criticality; exploitation not reported\.
- **affected:** yes
- **exposure:** internal
- **criticality:** standard
- **evidence ids:** \["demo-inventory-3", "demo-advisory-1"\]


## Limitations

- This is an original illustrative matrix, not CERT/CC SSVC, CVSS or an organizational severity policy\.
- Input evidence references are preserved but are not retrieved or independently authenticated\.
- Not reported does not establish that exploitation is absent\. Unknown facts never become a low-risk assumption\.
- Priorities carry no automatic patch deadline\. Controls, business impact and policy-specific obligations need review\.

## Next Steps

- Validate exposure, exploitation and business-criticality facts with dated evidence\.
- Have the asset owner assign a remediation target under the applicable policy\.
- Reassess when exploitation, exposure, evidence quality or control effectiveness changes\.
