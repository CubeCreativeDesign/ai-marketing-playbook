# Stage 1: Topic Development

## Purpose
Generate and refine blog topic ideas for K-12 private school marketing. This covers private, independent, faith-based, and virtual K-12 schools — but NOT home services or pest control (separate verticals).

## Who We Are
**Customize this:** Replace with your own agency description. This section tells Claude who you are so it writes from the right perspective.

Your agency markets TO private schools (as clients), not on behalf of schools to parents. Your content targets school administrators, marketing directors, and admissions teams who are evaluating whether to hire a marketing agency.

Secondary audience: Parent researchers evaluating schools (because schools share your content and it builds topical authority).

## Batch Mode
When processing from a batch table (see `reference/batch-template.md`), skip Step 1 entirely. Pull Topic, Primary Keyword, Secondary Keywords, Goal, Seasonal Tie-In, and Research/Notes directly from the table row and proceed to Step 2.

## Cross-Vertical Adaptation
When the user provides content from another vertical to adapt:
- Review the source content for structure, arguments, and data points
- Identify which elements translate directly to private schools and which need full replacement
- The user will specify whether to keep the same structure (swap industry specifics) or write fresh from the same angle
- Build the topic brief around the private school version, noting the source content as a reference

---

## Topic Generation Process

### Step 1: Ask for Direction
*Skip this step in batch mode — inputs come from the table.*

Ask the user:
- Do you have a specific topic in mind, or should I suggest options?
- Is this tied to a seasonal campaign? (See seasonal calendar in `reference/seasonal-calendar.md`)
- What's the primary goal: awareness, lead generation, or thought leadership?
- Is this being adapted from another vertical? If so, provide the source content.

### Step 2: Topic Validation
For any proposed topic, evaluate:
- **Search demand**: Is anyone searching for this? What keywords apply?
- **Competition**: Can we realistically rank for this?
- **Relevance**: Does this serve school admins/marketers specifically?
- **Differentiation**: Can we offer a unique angle vs. generic education marketing blogs?
- **School type flexibility**: Does this topic work across multiple school types, or is it specific to one? Note which types it applies to (college prep, faith-based, virtual, lower-cost, etc.).

### Step 3: Topic Brief
Output a brief that includes:
- Working title
- Primary keyword (1)
- Secondary keywords (2-3)
- Target audience (admin, marketer, admissions director, parent)
- Applicable school types (all private schools, or specific: faith-based, college prep, virtual, lower-cost, etc.)
- Content angle/hook
- Recommended word count (default 1,200; range 800-2,500)
- Suggested content balance: SEO-Heavy (70/30), Balanced (50/50), or Narrative-Heavy (30/70)

### Step 4: Deep Research Integration (Optional)
If the user provides Google Deep Research output or other research:
- Cross-reference the draft against research findings
- Identify data points, statistics, and trends worth including
- Flag anything the research covers that the brief missed
- Note any claims that need verification before publishing

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
- CRM for schools (HubSpot focus)
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
Save the completed topic brief to `output/[topic-slug]-brief.md`
