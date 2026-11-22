INSURANCE BUDDY — SUBMISSION DOCUMENT
Working outline, WAICY 2026, LLM & AI Agent Track

This is the order to write in. Each section says what to include, how long it
should be, and where your existing material goes. Sections marked [YOU WRITE]
are the graded prose. Leave them in your voice.

The final file must be one PDF named:
    LLM_InsuranceBuddy.pdf

==============================================================================
BEFORE YOU START: gather these
==============================================================================

Have these open while writing:

  1. Insurance_Buddy_User_Profiles.docx     (profiles, being edited)
  2. TASK6_CHAT_HISTORY.md                  (the conversation script)
  3. The chat screenshots                   (once you have the live app)
  4. Both links                              (chatbot URL + chat history link)
  5. The iteration log                       (v4 to v10 failures, listed below)

If you do not have the links yet, write every other section and leave two
placeholders. Do not invent links.

==============================================================================
SECTION ORDER — write in this order, not the document's order
==============================================================================

The document's order is fixed. The WRITING order below is chosen so that each
section is easier because the one before it exists.


------------------------------------------------------------------------------
1. WHAT SPECIFIC SERVICE YOUR AI PROVIDES
------------------------------------------------------------------------------
LENGTH: half a page to one page.

Write this first. Everything else refers back to it.

Include:
  - One sentence naming the advisor. Not "an AI health advisor". Something
    like: an advisor that tells a person which hospitals in their city accept
    their specific insurance class.
  - The problem in plain words: coverage in Saudi Arabia is set at CLASS level
    (Class A / Class B), not company level, and a hospital that accepts the
    company does not necessarily accept every class.
  - The value: the person finds out before travelling, not at the desk.
  - Why it is narrow: it does not give medical advice, does not recommend
    doctors, does not compare policies. It answers one question.

Do NOT:
  - Call it a general health assistant.
  - Claim it covers all insurers. Say plainly that not all of them publish
    the data, and that the advisor refuses when they do not.

Your strongest sentence, from your own scope work:
  "The advisor answers one question: which hospitals in your city accept my
   insurance class."


------------------------------------------------------------------------------
2. MOTIVATION
------------------------------------------------------------------------------
LENGTH: half a page.

Write this second. It is the only section where family stories belong.

Include:
  - What prompted the project. Your mum changed plans and had no way to
    check. Use it, but keep it short.
  - The finding from interviews: the information exists but is published
    inconsistently. Some insurers publish a network by class, most do not.
  - What people currently do instead: drive to the hospital and ask.

Quote your mum here if you have not used her quotes in the profiles section.
Do not use the same quote twice in the document.

Do NOT:
  - Claim the problem is healthcare quality. It is information access.
  - Overstate. "Some insurers publish nothing" is accurate; "insurers hide
    their networks" is not.


------------------------------------------------------------------------------
3. THE USERS — THREE PROFILES
------------------------------------------------------------------------------
LENGTH: one page for all three.

This is Insurance_Buddy_User_Profiles.docx, with Profile 3 completed.

Before pasting, confirm:
  - All placeholder brackets are deleted.
  - Dad's section does not claim more than he said.
  - Mum's quotes are word-for-word and unedited.
  - Profile 3 is written and is genuinely different from Profile 2.
  - No real names anywhere.


------------------------------------------------------------------------------
4. ITERATIVE AI DESIGN PROCESS
------------------------------------------------------------------------------
LENGTH: one and a half to two pages. This is worth 25% of the AI criteria.
         Do not rush it.

This is the section judges weight most heavily after the service description
itself. It needs FIVE stages, each with evidence:

  IDEA
    Where the idea came from. The interview finding: class-level coverage,
    inconsistently published. One paragraph.

  ADVISOR DESIGN
    The first version of the prompt and what it got wrong. Six versions were
    written; here is the honest log you already have:

    | Version | What changed | Why — the failure that forced it |
    |---------|--------------|----------------------------------|
    | v4      | starting point | asked five questions, one per message, so the user needed five turns before any answer |
    | v5      | gap-only questions | removed a question that carried no information |
    | v6      | person-first rule | v5 answered "I am sick" with a cold refusal |
    | v7      | class-mapping rule | the advisor said "cannot confirm" and then named three hospitals anyway |
    | v8      | explicit length rule | there was no length rule at all; answers were long |
    | v9      | fixed shape for refusals | v8 produced 174 words while claiming to be brief |
    | v10     | banned invented phone numbers | three runs produced three different Bupa numbers |

    Present this as a table. It is the clearest evidence of iteration you have.

  TESTING
    How you tested: role-playing each of the three profiles, plus adversarial
    questions. State the number of automated checks you ran (54) and that
    they pass.

  ERROR ANALYSIS
    The four real failures, each with what caused it:
      1. Cold refusal to "I am sick" — the prompt had no instruction to
         respond to the person before asking for data.
      2. Contradiction: said it could not confirm, then named hospitals. The
         rule allowed naming any hospital in the file. Now two conditions are
         required before a hospital may be named.
      3. Invented phone numbers — the model filled gaps the data did not have.
         Now no number may be stated unless it is in the table.
      4. A question about Al Khobar returned Riyadh hospitals. The city
         matcher only recognised the spelling "khobar", so "Alkhobar" fell
         through to the previous message. Fixed, and a regression test now
         fails if Riyadh appears in a Khobar answer.

  IMPROVEMENT
    What the final version does: answers most questions from the hospital
    tables with no model call at all (measured 0.1 to 7 milliseconds), and
    reaches the model only when the tables cannot settle the question. Refuses
    honestly rather than guessing.

  Put a screenshot of one before/after pair here if you have one.

Do NOT:
  - Invent test results. Only report what you actually ran.
  - Claim the model is always used. It is the last resort, and that is a
    strength worth stating.


------------------------------------------------------------------------------
5. LIMITATIONS
------------------------------------------------------------------------------
LENGTH: half a page. Five limitations, each two or three sentences.

These are already established, use them:

  1. NOT EVERY INSURER PUBLISHES THE DATA.
     Many carriers publish no provider network by class. For those, the
     advisor can only tell the user the information does not exist and send
     them to the desk. This is the largest limitation and it is deliberate:
     the alternative is inventing an answer.

  2. CLASS MAPPING IS INCOMPLETE.
     Some insurers publish network levels (NW1, NW2) that cannot be reliably
     mapped to Class A or Class B. Where the mapping is not in the source, the
     advisor refuses rather than converting a level into a class.

  3. THE DATA CAN GO STALE.
     Coverage lists change. The advisor reflects what was published when the
     tables were built, not today's contracts.

  4. IT IS NOT AN EMERGENCY SERVICE.
     It names 997 for emergencies but it does not triage. Someone with chest
     pain must not wait for the application.

  5. THE MODEL NEEDS CREDIT AND A KEY.
     The fallback path requires a paid API account. The table path does not,
     so the core function survives without it, but the free-text path does
     not.

Ethical note worth including, one sentence: the advisor must never name a
hospital it cannot verify, because a wrong answer to a health-insurance
question costs a person a wasted trip or an interrupted treatment.


------------------------------------------------------------------------------
6. FUTURE DEVELOPMENT
------------------------------------------------------------------------------
LENGTH: half a page. Each item must answer one limitation above.

The rubric checks that this section responds to the limitations directly.
Map them explicitly:

  1. ANSWERS LIMITATION 1 — a voice agent that telephones the hospital to
     confirm whether a given class is accepted, removing the user's trip
     entirely. This is designed but not built. Say so.

  2. ANSWERS LIMITATION 2 — ask the insurer directly for a class mapping,
     rather than inferring one from a published level.

  3. ANSWERS LIMITATION 3 — refresh the tables automatically and show the
     date each table was captured, so the user knows how current it is.

  4. ANSWERS LIMITATION 4 — clearer emergency routing: detect emergency
     language first and give 997 before anything else.

  5. ANSWERS LIMITATION 5 — run the fallback on a smaller local model so the
     application needs no paid account.

Do NOT claim any of these are built. All five are planned.


------------------------------------------------------------------------------
7. CONCLUSION
------------------------------------------------------------------------------
LENGTH: one paragraph, four to six sentences.

Summarise: the question the advisor answers, the finding that motivated it,
the evidence it refuses when it cannot verify, and what it changes for the
person who used to drive to the hospital to ask.

Do not introduce new claims here.


------------------------------------------------------------------------------
8. REFERENCES
------------------------------------------------------------------------------
LENGTH: as needed. APA style is fine.

List:
  - Each insurer's public provider locator you extracted data from. Name the
    insurer and the URL. There are 25; list the ones whose data is actually
    used in answers.
  - The Saudi Red Crescent Authority, for 997.
  - Any article or source you used when researching how Saudi health
    insurance classes work.
  - The tool documentation you relied on, if you cite it.

Do not list a source you did not open.

==============================================================================
APPENDED SECTIONS — required, easy to forget
==============================================================================

At the back of the PDF, or in the body, include:

  A. LINK TO THE CHATBOT
     The live Streamlit URL. Must open without logging in.

  B. LINK TO THE CHAT HISTORY
     At least 10 exchanged messages, on the FINAL version of the assistant.
     A script is not a chat history. It must be a real conversation.

  C. CHAT SCREENSHOTS
     Optional but persuasive. One screenshot of a refusal ("this insurer
     publishes no list") is worth a paragraph.

==============================================================================
CHECKLIST BEFORE EXPORTING THE PDF
==============================================================================

  [ ] Every section above is present, in the required order
  [ ] No placeholder text like [TO BE COMPLETED] or [square brackets]
  [ ] Both links open in a private browser window
  [ ] The chat history has 10 or more exchanges
  [ ] The chat history is on the final version, not an older draft
  [ ] No real names
  [ ] Future Development maps to Limitations one by one
  [ ] References list only sources actually used
  [ ] File is named LLM_InsuranceBuddy.pdf
  [ ] Page numbers on
  [ ] Consistent font throughout (Word default is fine)

==============================================================================
WHAT TO WRITE TONIGHT, IN ORDER
==============================================================================

  1. Section 1 (service)          — 20 min, write it in your own words
  2. Section 2 (motivation)       — 15 min
  3. Section 4 (iteration)        — 45 min, the table does most of the work
  4. Section 5 (limitations)      — 20 min
  5. Section 6 (future)           — 15 min, map to section 5
  6. Section 7 (conclusion)       — 10 min

Leave Section 3 (profiles) until your aunt replies, and the two links until
the deploy is possible. Everything else can be written now.
