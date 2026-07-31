| Question | Faithfulness | Context Precision | What it reveals |
|---|---|---|---|
| MSPPM vs MSPPM-DA | 0.60 | 0.00 | Retrieval pulled a page-footer fragment + MSPPM-DC content instead of DA content. Answer stayed "faithful" to bad context — faithfulness alone hid this. |
| AIM internship | 0.00 | 0.50 | Correctly detected no AIM-specific internship evidence → honest "I don't know." Low faithfulness here is a metric artifact (zero claims made), not a real failure. |
| MISM-BIDA extra classes | 0.57 | 1.00 | Retrieval nailed it; any remaining answer imperfection is a generation-layer issue, not retrieval. |
| Video games → MEIM | 0.86 | 0.33 | Answer sounded great and stayed grounded, but retrieval only got ~2-3 of 5 chunks genuinely on-topic. Good example of faithfulness masking mediocre retrieval. |
| MSIT vs MISM | 0.67 | 0.33 | Retrieval mixed real MSIT/MISM content with a header-only chunk and pure metadata lines — diluted precision despite a solid answer. |
| Gap year | 0.20 | 0.00 | Expected — the real answer isn't in this corpus at all (deferred to a document I don't have). Correctly flagged as a known corpus gap, not a bug. |
| Outside-Heinz classes | 0.67 | 1.00 | Retrieval excellent; matches grading note almost exactly. |
| Healthcare industry | 0.60 | 0.75 | Solid on both counts; MSHCA content retrieved well, though didn't rank MSHCA as clearly primary in the final answer. |
| Weather (out-of-scope) | 0.00 | 0.00 | Correct refusal. Retrieved chunks matched only on the literal word "Pittsburgh" (library, campus) — good concrete proof that dense embeddings match words, not topical relevance. System stayed honest anyway. |
| Add/drop deadline | 1.00 | 1.00 | Clean, simple factual question — both metrics agree it's a strong result. |