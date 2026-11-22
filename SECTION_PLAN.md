SECTION-BY-SECTION PLAN
Insurance Buddy — WAICY 2026, LLM & AI Agent Track

One page. What to write in each section, in order, with the facts you already
have. Tick a box when a section is done.


==============================================================================
SECTION 1 — WHAT SERVICE YOUR AI PROVIDES          [x] DONE
==============================================================================
Four paragraphs plus a closing line. Already written and pasted.

  P1  One sentence: answers which hospitals in my city accept my insurance class.
  P2  Coverage is set at class level, not company level.
  P3  Plan changes leave people without knowing where to go.
  P4  The chatbot asks insurer + class + city, looks up the published list,
      and refuses when the insurer publishes nothing.
  P5  Value: the person finds out before they travel.


==============================================================================
SECTION 2 — MOTIVATION                            [ ] TO WRITE  (half a page)
==============================================================================
Four short paragraphs.

  P1  WHAT STARTED IT
      Your mum changed insurance plans. Her card shows Class A or Class B,
      but nothing told her which hospitals the new plan covers.

  P2  WHAT SHE DOES INSTEAD
      She drives to the hospital and asks at the desk.
      Quote her here OR in Section 3 — not both:
      "I would have to find out through the category of my insurance and
       then I will go to the hospital and ask if it covers it or no."

  P3  WHAT THE INTERVIEWS SHOWED
      Three family members interviewed. Their answers differed by situation,
      not by age. The information exists but is published inconsistently:
      some insurers publish a network by class, most do not.

  P4  WHY IT MATTERS
      For someone with a chronic condition, a plan change can interrupt
      treatment, not just cost a trip.

  RULES
      - Do not say the healthcare system is bad. That is not the claim.
      - Do not say insurers "hide" information. Say "publish inconsistently".
      - Do not claim a large survey. You interviewed three family members.


==============================================================================
SECTION 3 — THREE USER PROFILES                    [ ] WAITING ON AUNT
==============================================================================
Paste from Insurance_Buddy_User_Profiles.docx once Profile 3 is written.
One page for all three.

  BEFORE PASTING
      - Delete every placeholder bracket
      - Dad must not claim more than he said
      - Mum's quotes word-for-word, unedited
      - Profile 3 written and genuinely different from Profile 2
      - No real names


==============================================================================
SECTION 4 — ITERATIVE AI DESIGN PROCESS            [ ] TO WRITE  (1.5-2 pages)
==============================================================================
Worth 25% of the AI criteria. Five subsections.

  4.1  IDEA
       Where it came from: the interview finding — class-level coverage,
       inconsistently published. One paragraph.

  4.2  ADVISOR DESIGN
       One or two sentences, then the version table (already in the skeleton).

  4.3  TESTING
       Role-played each of the three profiles. Asked adversarial questions.
       State: 54 automated checks, all passing.
       Do not invent results. Only what you actually ran.

  4.4  ERROR ANALYSIS
       The four failures, each with its cause (already in the skeleton):
         1. Cold refusal to "I am sick"
         2. Said "cannot confirm", then named hospitals
         3. Three different invented Bupa phone numbers
         4. Al Khobar question returned Riyadh hospitals

  4.5  IMPROVEMENT
       Tables first (0.1-7 ms). Model only as last resort. Honest refusal
       instead of a guess.


==============================================================================
SECTION 5 — LIMITATIONS                           [ ] TO WRITE  (half a page)
==============================================================================
Five limitations plus one ethical paragraph. Two or three sentences each.
Headings are already in the skeleton; write the body under each.

  5.1  Not every insurer publishes the data.      <- the largest one
  5.2  Class mapping is incomplete.
  5.3  The data can go stale.
  5.4  It is not an emergency service.
  5.5  The model needs credit and a key.
  5.6  Ethical considerations.

  TEST for each paragraph: "would this exist if the chatbot didn't?"
  If no, you are pasting the bot's output instead of writing analysis.


==============================================================================
SECTION 6 — FUTURE DEVELOPMENT                    [ ] TO WRITE  (half a page)
==============================================================================
Five items. Each answers one limitation. Keep the numbering aligned:
1->1, 2->2, and so on. The rubric checks this link directly.

  A voice agent that telephones the hospital to confirm a class.
  Say "designed, not built". Do not claim it exists.


==============================================================================
SECTION 7 — CONCLUSION                            [ ] TO WRITE  (4-6 sentences)
==============================================================================
One paragraph: the question, the finding, the refusals, what changes for the
user. Introduce no new claims.


==============================================================================
SECTION 8 — REFERENCES                            [ ] TO WRITE
==============================================================================
  - Each insurer's public provider locator you extracted data from
  - Saudi Red Crescent Authority, for 997
  - Any research source you actually opened
  Do not list a source you did not open.


==============================================================================
APPENDIX — THE TWO LINKS                          [ ] BLOCKED ON DEPLOY
==============================================================================
  - Link to the chatbot (live Streamlit URL)
  - Link to the chat history (10+ exchanges, on the FINAL version)


==============================================================================
ORDER TO WRITE IN, AND WHY
==============================================================================
  1. Section 2   (15 min)  — you know the story already
  2. Section 4   (45 min)  — the table is pre-filled; write around it
  3. Section 5   (20 min)  — five short paragraphs
  4. Section 6   (15 min)  — mirrors section 5
  5. Section 7   (10 min)  — summary only
  6. Section 3   (when your aunt replies)
  7. Section 8   (last; gather URLs as you go)
  8. Links       (when the repo is public)

Total writing time: about two hours, excluding Section 3 and the links.
