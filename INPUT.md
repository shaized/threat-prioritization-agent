# Input and output contract

## Input

The root requires threat_id, exploitation (active/not_reported/unknown), and assets. Each asset requires unique id, affected (yes/no/unknown), exposure (internet/internal/unknown), criticality (high/standard/unknown) and evidence_ids. Known affected states require nonempty references. References are preserved but not dereferenced. Decision order: no→verify non-applicability; unknown→investigate; affected plus active exploitation→urgent; any remaining unknown→resolve facts; internet plus high criticality→urgent; either→expedited; otherwise→scheduled. All outputs require human review.

See [example.json](example.json) for a complete fictional input. All demo identities, indicators, events, products and reputation providers are synthetic. Documentation IPs and example domains are not threat intelligence.

Input must be a UTF-8 JSON object no larger than 2 MiB. Duplicate JSON keys, malformed required fields, ambiguous timestamps and conflicting identifiers are rejected. Timestamps require an explicit UTC offset. Small local snapshots are the intended workload; there is no streaming, database or production connector in this version.

## Output

`python3 agent.py INPUT.json` emits Markdown. Add `--format json` for structured output. The JSON envelope contains schema_version, agent, summary, findings, limitations and next_steps. The tool writes to standard output and does not modify the source input. Input errors return exit code 2; a valid assessment returns 0 even when findings are present.

JSON preserves evidence text. Markdown renders evidence as literal escaped text, so input cannot inject links, headings or HTML into the report. Every result preserves substantive limitations.

## Example interpretation

An urgent review, an exposure investigation and a scheduled review, each with a stated reason. No patch deadline is fabricated.

The matrix is an original teaching example. Replace it with an approved policy before operational use; it does not implement CERT/CC SSVC.
