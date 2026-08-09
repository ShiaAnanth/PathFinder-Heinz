| Question | Faithfulness | Context Precision | What it reveals |
|---|---|---|---|
| What is the difference between the msppm and the msppm-da programs? | 0.60 | 0.00 | Retrieval pulled a page-footer fragment + MSPPM-DC content instead of DA content. Answer stayed "faithful" to bad context — faithfulness alone hid this. |
| Does AIM have an internship requirement? | 0.00 | 0.50 | Correctly detected no AIM-specific internship evidence → honest "I don't know." Low faithfulness here is a metric artifact (zero claims made), not a real failure. |
| What extra core classes do I need for MISM BIDA compared to MISM? | 0.57 | 1.00 | Retrieval nailed it; any remaining answer imperfection is a generation-layer issue, not retrieval. |
| I am interested in managing and designing video games, which program should I choose? | 0.86 | 0.33 | Answer sounded great and stayed grounded, but retrieval only got ~2-3 of 5 chunks genuinely on-topic. Good example of faithfulness masking mediocre retrieval. |
| How is MSIT different from MISM? | 0.67 | 0.33 | Retrieval mixed real MSIT/MISM content with a header-only chunk and pure metadata lines — diluted precision despite a solid answer. |
| Can I take a gap year? | 0.20 | 0.00 | Expected — the real answer isn't in this corpus at all (deferred to a document I don't have). Correctly flagged as a known corpus gap, not a bug. |
| How do I take classes outside of Heinz college? | 0.67 | 1.00 | Retrieval excellent; matches grading note almost exactly. |
| I want to break into the health care industry, what should I pursue? | 0.60 | 0.75 | Solid on both counts; MSHCA content retrieved well, though didn't rank MSHCA as clearly primary in the final answer. |
| What is the weather like in Pittsburgh? | 0.00 | 0.00 | Correct refusal. Retrieved chunks matched only on the literal word "Pittsburgh" (library, campus) — good concrete proof that dense embeddings match words, not topical relevance. System stayed honest anyway. |
| What is the add drop deadline? | 1.00 | 1.00 | Clean, simple factual question — both metrics agree it's a strong result. |
