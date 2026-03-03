# Climate change knowledge bot: feasibility analysis

**Date:** 3 March 2025  
**Context:** AI bot for climate change knowledge; RAG over Climate Academy, semantic IPCC, encyclopedia, and optional scholarly literature. Multilingual (English, Hindi, Urdu). Qwen3.5. Ground-truth indication per statement.

---

## Summary

**Feasibility: yes.** The proposed approach is feasible. RAG over curated sources with a clear primary source (Climate Academy) and optional tiers (IPCC, encyclopedia, literature) is a standard, controllable pattern. Indicating ground truth per statement via citations/source labels is achievable. Qwen3.5 supports the target languages. Scope (elementary, factual) is appropriate. amilib aligns with building and maintaining the knowledge base.

---

## Why it is feasible

1. **RAG fits the use case**  
   Retrieval-augmented generation over your own documents (Climate Academy, IPCC, encyclopedia, optionally literature) is a proven way to anchor answers to sources and reduce hallucination. It suits an “elementary, factual” scope well.

2. **Clear ground truth and guardrails**  
   Using the 350-page Climate Academy book as the primary reference and guardrail gives a single, coherent “voice” and a natural definition of ground truth. The semantic IPCC corpus and the encyclopedia can sit alongside as additional evidence, with the option to rank or tag by source (e.g. “from Climate Academy” vs “from IPCC” vs “from encyclopedia”).

3. **“Ground truth” per statement is achievable**  
   With RAG you can attach a source (and optionally a label such as “Climate Academy” / “IPCC” / “Encyclopedia”) to each retrieved chunk and ask the model to cite or tag statements accordingly. Indicating the ground truth of each statement is feasible without changing the high-level architecture—it is mainly retrieval design and response formatting.

4. **Multilingual (English, Hindi, Urdu)**  
   Qwen3.5 has strong multilingual and Indic-language support. Serving the same RAG content in English, Hindi, and Urdu is realistic; the main design choice is whether you index/retrieve in one or several languages and then translate or generate in the user’s language.

5. **Scope is well chosen**  
   Starting with elementary, factual questions keeps complexity and controversy manageable and makes it easier to validate answers against Climate Academy and the encyclopedia.

6. **Alignment with amilib**  
   amilib’s workflows (dictionaries/encyclopedias, corpus handling, HTML/PDF, and potential for semantic/structured content) are compatible with building and maintaining the knowledge base (encyclopedia, IPCC-derived content) that the RAG system would use.

---

## Things to be aware of (no details yet)

- **Source hierarchy:** Decide how to combine or prioritise Climate Academy vs IPCC vs encyclopedia vs literature so that “ground truth” and guardrails are unambiguous.
- **Retrieval strategy:** One index vs tiered retrieval (e.g. Climate Academy first, then others) will affect how clearly you can label “ground truth”.
- **Multilingual strategy:** Whether you do multilingual retrieval, translation of chunks, or only multilingual generation will affect quality and complexity.

---

## Next step

The approach is feasible. Next step is to fix the source hierarchy and high-level RAG design (what to index, in what order to use it, and how to tag “ground truth”), then drill into details.
