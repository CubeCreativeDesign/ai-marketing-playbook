# Prompt: Build Reader Personas

Paste everything below this line into a new Claude conversation.

---

I need your help building reader persona profiles for a blog content pipeline. These personas describe the business owners and operators I'm writing for — their company size, goals, frustrations, and how they think about marketing. The pipeline uses these to calibrate tone, examples, pain points, and budget assumptions for every post.

## What we're building

A `reader-personas.md` file with one persona per company size tier you serve. Each persona includes:
- Business demographics (size, revenue, service area)
- Owner/decision-maker profile
- Goals and pain points
- Current marketing approach
- What they need to see before hiring an agency
- A short "Day in the Life" narrative
- Fictional company details for use in blog examples

## Step 1 — Tell me about your clients

Answer as many of these as you can:

1. What industry do your clients work in?
2. What size companies do you typically work with? (employees, revenue, number of locations)
3. What are the most common reasons clients come to you? What problem are they trying to solve?
4. What objections do you hear most often during the sales process?
5. What does a good client look like? What does a frustrating one look like?
6. What's the biggest misconception your clients have about marketing when they first come to you?
7. Are there distinct "types" of client you serve — e.g., the scrappy startup vs. the established owner who's ready to scale?

## Step 2 — Paste real client communications (optional but highly recommended)

If you have any of the following, paste them in. This is what turns a generic persona into something that actually matches the people you work with:

- Emails from clients describing their situation or asking for help
- Discovery call notes or CRM records
- Proposal feedback or objection emails
- Testimonials or review text
- Onboarding questionnaire responses
- Any message where a client described their own business in their own words

Anonymize anything sensitive — replace company names with "Client A" etc. The content is what matters, not the names.

## Step 3 — Define your size tiers

Tell me how you segment your clients by size. For example:
- Startup: 1–5 employees
- Growing: 5–15 employees
- Established: 15–50 employees

Or just describe your smallest, typical, and largest client and I'll build the tiers from that.

## Step 4 — Fictional reference companies

For each persona tier, I'll also create a fictional company to use in blog post examples (e.g., "Metro Comfort HVAC, a 12-person shop in Columbus"). Tell me:

1. What region or city should the fictional companies be based in? (Use your primary service area)
2. Any naming conventions you want — realistic business names, or generic placeholders?

## Step 5 — Review and refine

I'll draft one persona at a time and show it to you. For each:
- Tell me if the "Day in the Life" narrative rings true
- Tell me if the pain points and goals match what you actually hear
- Tell me if the budget/revenue figures are realistic for that tier

## Output format

When we're done, I'll produce a complete `reader-personas.md` file ready to drop into your project's `reference/` folder. Each persona will follow this structure:

```
# [YOUR_VERTICAL] Business Owner Persona: [Size Tier]

## Persona: [Name], "[Archetype Label]"

### Business Demographics
- Company size, revenue, service area, services offered

### Owner Profile
- Background, how they got here, what their day looks like

### Goals & Pain Points
- Growth goals, operational struggles, marketing frustrations

### Current Marketing Approach
- What they're doing now, what's working, what isn't

### Decision Factors for Hiring an Agency
- What they need to see, what makes them hesitate

### Day in the Life
[2–3 paragraph narrative grounded in their operational reality]

### Fictional Reference Company
[Name, location, size, key contact — for use in blog examples]
```

---

Ready when you are. Start with Step 1 or paste client communications directly — I'll work with whatever you give me.
