# HANDOFF: AI Marketing Playbook

Public repo `yoderman94/ai-marketing-playbook`. Every public Claude template lives here as a folder. Last updated 2026-10-09.

## Layout and ownership
- `projects/`: paste-in Claude Project templates.
- `cowork/private-schools/`: Cowork pipeline, Stage 0 plus 8 content stages, no scripts. Refreshed 2026-10-09 from the production schools pipeline (v1.14.0) and made generic.
- `claude-code/b2b-blog-pipeline/`: the scripted pipeline, v2.0.2. It has its own VERSION, CHANGELOG and HANDOFF. It moved here from the standalone `b2b-blog-pipeline-template` repo, which is now archived. Fix it here.

## Deliberate choices
- The author byline and the agency links appear only in the top-level README, CLAUDE.md and LICENSE. Template folders use `[YOUR_...]` placeholders.
- The Cowork pipeline has no QC script. Stages 2 and 3 write a Self-Check block that Claude fills by judgment. Stage 3 replaces the Stage 2 block.
- `reference/k-12-private-school-personas.md` and `k-12-private-school-competitors.md` stay templates. Never fill them with real client data.
- Two reader persona templates exist on purpose: the long guide in `k-12-private-school-personas.md` and the short `READER-PERSONA-TEMPLATE.md`. Each points to the other.
- The `projects/titles-meta-keywords.md` limits (60 characters, 160 for the meta) are maximums. The pipelines aim lower (title about 55).

## Open items
- The b2b Stage 4 meta template still ends in "[Why from us/CTA]". Check it against the no-phone-CTA rule.
- Nothing in `cowork/` has been run end to end in Cowork since the refresh.

## Before every commit
Run the deny-list grep and `gitleaks dir .` (see CLAUDE.md). The repo is public, so every push needs the owner's OK.
