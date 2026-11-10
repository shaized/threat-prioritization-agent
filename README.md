# Threat Prioritization Agent

**Make remediation priorities explainable and uncertainty explicit.**

A model-agnostic AI agent skill paired with a working Python evidence tool. The skill guides an assistant's analysis; the deterministic tool validates and organizes a local evidence snapshot. The included demo runs offline with no API key or dependencies.

[Agent instructions](SKILL.md) · [Example report](example-report.md) · [Input contract](INPUT.md) · [Portfolio](https://shaized.github.io/)

## Try it in one minute

Requires Python 3.11 or newer.

```sh
git clone https://github.com/shaized/threat-prioritization-agent.git
cd threat-prioritization-agent
python3 agent.py example.json
python3 agent.py example.json --format json
python3 -m unittest discover -v
```

**Expected result:** An urgent review, an exposure investigation and a scheduled review, each with a stated reason. No patch deadline is fabricated.

## Use it as an AI agent

Open the repository in an assistant that can read local files and run Python, then give it this request:

> Read SKILL.md and follow its workflow. Prioritize review of the fictional assets in example.json. Explain every decision, distinguish unknown facts from lower risk and avoid inventing remediation deadlines.

SKILL.md is the agent entry point. INPUT.md defines the evidence contract. agent.py performs the domain-specific analysis; runtime.py handles bounded JSON input, validation and report rendering. The assistant can explain the results, investigate alternatives and identify missing evidence using the tools you authorize.

The Python command itself is **not an LLM runtime**. It makes no network calls and performs no operational actions. There is no bundled model, production connector, autonomous service or implied access to your environment.

## What the agent does

1. Confirm the specific threat, assessed assets and evidence supporting affected status, exploitation, exposure and criticality.
2. Use agent.py to apply the documented example matrix. Treat its result as a review queue, not an official SSVC, CVSS, severity or SLA decision.
3. Investigate unresolved facts and explain how new evidence could change the outcome. A compensating control only changes a real policy assessment when its applicability and effectiveness are verified.
4. Present per-asset reasoning, evidence gaps, ownership and reassessment triggers. Use the user's actual policy when supplied and make any departure from the example matrix explicit.

## Design

```text
Selected evidence → validated local tool → traceable report
                                             ↓
                         AI-assisted reasoning → analyst decision
```

The examples are original, vendor-neutral implementations. All bundled data is fictional. Results retain unknowns and evidence gaps rather than presenting missing data as reassurance. Read the input contract for exact matching, thresholds and limitations.

## Validate and extend

The test suite covers the example, meaningful boundary cases, invalid evidence references where applicable, timestamp handling, bounded input and safe Markdown output. GitHub Actions runs the same offline tests. To add a real integration, produce the documented input shape in a separately reviewed adapter; keep credentials and operational evidence outside this repository.

The matrix is an original teaching example. Replace it with an approved policy before operational use; it does not implement CERT/CC SSVC.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Use synthetic fixtures in issues and pull requests. This is a focused reference implementation; validate it against your data and review workflow before operational use.

## License

[MIT](LICENSE) · Built by [Shai Zaidenberg](https://github.com/shaized)
