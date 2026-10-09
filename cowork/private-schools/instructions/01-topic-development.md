# Stage 1: Topic Development

Stage 1 turns a topic and its Stage 0 research bundle into a topic brief that fixes the keywords, audience, angle and length for the post.

**Output feeds:** Stage 2 accepts this brief as settled. It does not re-decide the keywords, audience, content balance or word count, so make those calls here. Stage 4 builds titles around the primary keyword you pick, and Stage 5 builds the URL from it.

**Human check:** You, in the Cowork chat. In interactive mode, read the brief before Stage 2 starts and change anything that's off. In batch mode Claude does not stop, so put any concern (a weak keyword, thin research, a topic that overlaps a post you already have) in a `Notes for review` line at the end of the brief.

## Purpose
Generate and refine blog topic ideas for K-12 private school marketing. This covers private, independent, faith-based, and virtual K-12 schools. Other verticals you serve belong in their own Cowork projects.

## Who We Are
[YOUR_AGENCY] is a digital marketing agency that markets TO private schools (as clients), not on behalf of schools to parents. Our content targets school administrators, marketing directors, and admissions teams who are evaluating whether to hire a marketing agency.

Secondary audience: Parent researchers evaluating schools (because schools share our content and it builds topical authority).

**Customize this:** Replace [YOUR_AGENCY] with your agency name, and add a sentence or two about where you're based and who you serve. This section tells Claude whose voice the post is written in.

## Batch Mode
When processing from a batch table (see `batch-template.md`; the active queue is `batch-queue.md`), skip Step 1 entirely. Pull Topic, Primary Keyword, Secondary Keywords, Goal, Seasonal Tie-In, and Research/Notes directly from the table row and proceed to Step 2. Stage 0 has already run on the row's topic, so its bundle is waiting in `research/`.

## Cross-Vertical Adaptation
When the user provides content from another vertical to adapt:
- Review the source content for structure, arguments, and data points
- Identify which elements translate directly to private schools and which need full replacement
- The user will specify whether to keep the same structure (swap industry specifics) or write fresh from the same angle
- Build the topic brief around the private school version, noting the source content as a reference

---

## Topic Generation Process

### Step 1: Ask for Direction
*Skip this step in batch mode. Inputs come from the table.*

Ask the user:
- Do you have a specific topic in mind, or should I suggest options?
- Is this tied to a seasonal campaign? (See the seasonal calendar in `reference/seasonal-calendar.md`.)
- What's the primary goal: awareness, lead generation, or thought leadership?
- Is this being adapted from another vertical? If so, provide the source content.

### Step 2: Topic Validation
For any proposed topic, evaluate:
- **Search demand**: Is anyone searching for this? What keywords apply?
- **Competition**: Can we realistically rank for this?
- **Relevance**: Does this serve school admins and marketers specifically?
- **Differentiation**: Can we offer a unique angle vs. generic education marketing blogs?
- **School type flexibility**: Does this topic work across multiple school types, or is it specific to one? Note which types it applies to (college prep, faith-based, virtual, lower-cost, etc.).
- **Existing coverage**: Do you already have a post on this? If you can see your published posts (a sitemap, a blog index page, or a list the user shares), check them. A new post should take a different angle or replace the old one, not repeat it.

**Interactive mode, no research yet:** If the topic was just chosen in this chat, stop here and run Stage 0 (`instructions/00-deep-research.md`) on it. Come back to Step 3 once the research bundle passes its gate.

### Step 3: Topic Brief
Read the Stage 0 research bundle, `research/[topic-slug]-research.md`, before you write the brief. Use the topic slug Stage 0 created.

Output a brief that includes:
- Working title
- Topic slug (the same one Stage 0 used)
- Primary keyword (1)
- Secondary keywords (2-3)
- Target audience (admin, marketer, admissions director, parent)
- Applicable school types (all private schools, or specific: faith-based, college prep, virtual, lower-cost, etc.)
- Content angle/hook
- Recommended word count (default 1,200; range 800-2,500)
- Suggested content balance: SEO-Heavy (70/30), Balanced (50/50), or Narrative-Heavy (30/70)
- Research bundle: `research/[topic-slug]-research.md`
- Strongest evidence: the 3-5 verified quotes or statistics from the bundle that the angle rests on
- Notes for review (batch mode, or any time something needs a human look)

### Step 4: Research Integration
The Stage 0 bundle is the post's primary evidence. While you build the brief:
- Shape the angle around what the research can actually support. A strong angle with no verified evidence behind it becomes a weak post.
- Identify the data points, statistics, and trends worth including, and list the best ones in the brief.
- Flag anything the research covers that the brief missed.
- Never build the angle on an item the bundle tags `unverified`. If the topic needs a claim the bundle couldn't confirm, note it in the brief so Stage 2 verifies it or writes around it.
- If the user attached extra research (a report, survey results, a Research/Notes link), cross-reference it against the bundle and note any claims that still need verification before publishing.

## Topic Categories

### Enrollment & Admissions Marketing
- Enrollment funnel optimization
- Application process improvement
- Open house and campus visit promotion strategies
- Shadow day and accepted student event marketing
- Admissions yield improvement tactics
- Wait list communication strategies
- Inquiry-to-enrollment conversion optimization

### School Website & Digital Presence
- Website essentials for private schools
- Mobile optimization for school websites
- Program page strategies that convert visitors to inquiries
- Virtual tour and video integration
- Website speed and performance for school sites
- Tuition page strategy and transparency

### SEO & Online Visibility for Schools
- Local SEO for private schools
- Google Business Profile optimization for schools
- Search ranking strategies for enrollment keywords
- Content strategies that build topical authority
- Map pack strategies for schools competing locally

### AI & Technology for Schools
- AI tools for school marketing teams
- AI-powered admissions and follow-up
- Chatbots and automated inquiry response
- AI content strategies for school marketing
- How AI is changing how parents search for schools
- CRM for schools
- Marketing automation for admissions

### Social Media & Content Strategy
- Social media strategies for private schools
- Video marketing for school enrollment
- Parent testimonial content that generates inquiries
- Student spotlight and campus life content
- Community engagement through social media
- Managing school reputation on social platforms

### Email Marketing & Family Communication
- Email marketing for admissions and enrollment
- Parent communication best practices
- Re-enrollment campaign strategies
- Drip campaigns for prospective families
- Newsletter strategies that keep families engaged
- Welcome series for new families

### Retention & Re-enrollment
- Family retention strategies
- Re-enrollment campaign planning and timing
- Parent satisfaction and feedback systems
- Building community that keeps families enrolled
- Reducing attrition at key transition points (K to 1st, 5th to 6th, 8th to 9th)

### Brand Building & Reputation
- School brand differentiation in competitive markets
- Online review strategy for private schools
- Building trust with prospective families
- Communicating value proposition vs. tuition cost
- Reputation management for schools
- Crisis communication planning

### Event Marketing & Open Houses
- Open house planning and promotion
- Virtual event strategies for admissions
- Fundraising event marketing (galas, giving days)
- Back-to-school event campaigns
- Alumni event marketing

### Financial Aid & Tuition Communication
- Communicating financial aid effectively
- Tuition transparency strategies
- Scholarship marketing to attract diverse families
- Overcoming the "sticker shock" objection
- ROI of private education messaging
- School choice programs (vouchers, education savings accounts, tax-credit scholarships). Rules differ by state and change often, so check your state's current program pages before you build a topic on them.

### Lead Generation & Conversion
- Landing page strategies for school admissions
- Call tracking and inquiry attribution
- Pay-per-click advertising for enrollment
- Lead nurture sequences for prospective families
- Retargeting strategies for school websites

### Seasonal & Campaign Marketing
- Enrollment season campaign strategies
- Re-enrollment push timing and tactics
- Summer engagement to stay top-of-mind
- Back-to-school content campaigns
- Year-end giving and annual fund marketing

## Output
Save the completed topic brief to `output/[topic-slug]-brief.md`.
