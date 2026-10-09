# CLAUDE.md — AI Marketing Playbook

## Project Overview
This is a public GitHub repository maintained by Chad at Cube Creative Design. It contains practical AI workflows, Claude Project instructions, prompt templates, and automation configurations designed for digital marketing agencies, pest control marketers, and small business owners.

## Audience
- Conference attendees (PCT School, MAICON, chamber events)
- Digital marketing agency owners
- Small business owners exploring AI
- Pest control company marketers

## Tone & Style
- Conversational, practical, no-BS — like explaining something to a smart friend over coffee
- Use analogies that resonate with blue-collar business owners and marketers
- Avoid jargon unless it's defined immediately
- Include "why this matters" context, not just "how to do it"
- Dad jokes are welcome but not required

## Current File Organization

Every template is a self-contained folder. A reader copies one folder out and uses it on its own, so a folder must never depend on files outside itself.

```
ai-marketing-playbook/
├── README.md                          # Overview, who I am, index of every template
├── CLAUDE.md                          # This file (project instructions for Claude Code)
├── CHANGELOG.md                       # Repo-level change log
├── LICENSE                            # MIT License
│
├── getting-started/
│   └── README.md                      # Chat vs Projects vs Cowork vs Claude Code
│
├── projects/                          # Claude Project templates (paste-in instructions)
│   ├── README.md
│   ├── titles-meta-keywords.md
│   ├── check-links.md
│   ├── create-optimize-prompts.md
│   └── prompt-check.md
│
├── cowork/
│   └── private-schools/               # Stage 0 + 8 content stages, K-12 schools, no code
│
└── claude-code/
    └── b2b-blog-pipeline/             # Scripted batch pipeline (own VERSION, CHANGELOG, HANDOFF)
```

## Adding a New Template
- Put it in the folder for the tool it runs in: `projects/`, `cowork/`, or `claude-code/`.
- Add a row to the "What's Inside" table in `README.md` and a line to `CHANGELOG.md`.
- A pipeline folder keeps its own `.gitignore` for `output/`, `research/` and similar. Use the `output/*` form with `!output/.gitkeep`, never `output/`, or the negation can't work.

## Content Guidelines
- Each markdown file should start with a clear title and a one-sentence description of what it contains
- Include a "Who This Is For" note when relevant
- Use code blocks (```) for any prompt text or system instructions
- Add practical examples — show the input AND the expected output
- Link between files when topics overlap (use relative links)

## When Editing
- Keep the README.md table of contents updated when adding new files
- Maintain consistent heading structure (H1 for title, H2 for sections, H3 for subsections)
- Test all relative links between files
- Don't include any client-specific or proprietary information. Keep examples generic or use fictional company names.
- Chad's byline and the Cube Creative Design links in the top-level README are intentional. Inside template folders, use placeholders such as `[YOUR_AGENCY]` and `[YOUR-AGENCY-DOMAIN]` instead.

## Before Every Commit
This repo is public. Before you commit:
1. Grep for internal paths and names: home-directory paths, private repo names, client names, staff names, API keys, and cloud-drive links. Expect zero hits inside template folders.
2. Run `gitleaks dir .` and expect "no leaks found".
3. Check that every relative link and every file path a stage file cites exists.
