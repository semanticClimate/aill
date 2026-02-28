# Ingesting ~20k Climate HTML Pages for Local Q&A on M2 Mac

**Context:** ~20,000 pages of climate-change HTML with IDs and clear syntax/semantics. Goal: ingest into a system that runs **standalone on an M2 Mac with GPU**, open source, EN query → EN answer. **No generative AI** (retrieval / understanding only).

**Date:** 2025-02-28

---

## 1. Recommended approaches (in order)

### A. **Retrieval-only (no LLM)** — best fit for “no generative AI”

- **Idea:** Embed the HTML corpus (chunked by your semantics/IDs), embed user questions, run vector (and optionally keyword) search, return the **retrieved passages** as the “answer” (optionally reranked or lightly formatted).
- **Pros:** No generative model; deterministic; runs well on M2; minimal dependencies; full control over what is returned.
- **Cons:** “Answer” is always a subset of the corpus (no paraphrasing or synthesis).

**Stack suggestion:**

| Component        | Option 1 (simplest)     | Option 2 (MLX-native)     |
|-----------------|-------------------------|----------------------------|
| Embeddings      | sentence-transformers  | mlx-embeddings / mlx-embedding-models |
| Vector store    | ChromaDB or FAISS       | Same                       |
| Backend         | Python (PyTorch/MPS)    | Python + MLX (Metal GPU)  |

### B. **RAG with optional small LLM** (if you later want one-sentence answers)

- **Idea:** Same retrieval as above, then optionally pass top-k chunks to a **small local LLM** only to turn “these passages” into a short EN answer (no creative generation).
- **Pros:** Natural-language answers; still fully local and open source.
- **Cons:** Needs a small LLM (e.g. 3B–8B) and more RAM/GPU; “no generative AI” might be interpreted as excluding this.

**Local inference on M2 (open source):**

- **Ollama** — easy install, Metal-backed, many small models (e.g. Llama 3.2 3B, Phi, Mistral).
- **llama.cpp** (Metal) — lightweight, OpenAI-compatible `/v1/embeddings` and completion.
- **MLX / vLLM-MLX** — Apple Silicon–optimised; good for both embeddings and small LMs.

### C. **Fine-tuning a small model** (only if you have many query–answer pairs)

- **Idea:** Create (query, answer) or (query, best_chunk) pairs from your HTML + IDs, then fine-tune a small encoder or LM on M2 (e.g. via MLX-LoRA, or LoRA with PyTorch).
- **Pros:** Can capture domain phrasing and your ID/semantic structure very well.
- **Cons:** Needs curated training data and more engineering; overkill if retrieval-only already suffices.

### D. **Hybrid / “newer” options**

- **Hybrid search:** Combine **vector similarity** (semantic) with **keyword/BM25** (e.g. your IDs, terms). Libraries: LangChain/LlamaIndex retriever composition, or custom (e.g. FAISS + keyword filter).
- **Use your structure:** Your “clear syntax and semantics” and IDs are an advantage. Chunk by sections/IDs, store metadata (section id, doc id) with each embedding so answers can be tied to exact pages/sections.
- **Reranking:** After retrieval, use a small cross-encoder or reranker (many open-source options) to improve order of top-k before returning.

---

## 2. Suggested system (retrieval-only, M2, open source)

Target: **retrieval-only, EN in → EN out (returned passages), no generative AI.**

### Pipeline

1. **Ingest HTML**
   - Use your existing tooling (e.g. amilib-style HTML parsing) to:
     - Parse HTML, respect structure (headings, sections).
     - Extract or preserve **IDs** and semantics (e.g. section, chapter, document).
   - **Chunking:** Prefer **semantic chunking** (e.g. by `<section>`, heading levels, or fixed size with overlap) so each chunk has a stable ID and optional metadata (doc_id, section_id, title).

2. **Embeddings**
   - **Option A:** `sentence-transformers` (e.g. `all-MiniLM-L6-v2` or `BAAI/bge-small-en-v1.5`) with MPS on M2.
   - **Option B:** **MLX**-based embeddings (`mlx-embeddings` or `mlx-embedding-models`) for maximum M2 GPU use and no PyTorch dependency.
   - Embed each chunk; store **chunk text**, **IDs**, and **metadata** with the vector.

3. **Vector store**
   - **ChromaDB** or **FAISS** (both open source, work well locally).
   - Index embeddings; keep metadata (IDs, doc/section, snippet) for result presentation.

4. **Query path**
   - Embed the user’s EN query with the **same model**.
   - Run **k-NN** (e.g. top 5–20 chunks).
   - Optionally: **rerank** (e.g. cross-encoder), then return top chunks as the “answer” (formatted with your IDs and semantics).
   - Optional: add **keyword/BM25** over your IDs or terms and combine with vector scores (hybrid).

5. **No LLM** — the “answer” is the ranked list of passages (and their IDs); you can format them in EN (e.g. “According to section X: …”) without any generative model.

### Stack summary (all open source)

- **Language:** Python 3.10+
- **Embeddings:** sentence-transformers (MPS) **or** mlx-embeddings / mlx-embedding-models
- **Vector DB:** ChromaDB or FAISS
- **Optional:** LlamaIndex or LangChain for retriever/pipe structure, or minimal custom code
- **HTML:** Your existing pipeline (amilib-style) for parsing and chunking with IDs

### Scale (20k pages)

- 20k pages → roughly 50k–200k chunks depending on chunk size. FAISS/ChromaDB handle this easily on 16–32 GB RAM; embedding can be batched (e.g. 64–256 texts per batch) and run once at ingest.

---

## 3. If you later add a small LLM (still no “creative” generation)

- Run **Ollama** or **llama.cpp** (Metal) on M2 with a small model (e.g. 3B).
- Use it only to **compress** the retrieved chunks into a short EN answer (e.g. “Based on the following: …”) with a strict system prompt (“only use the provided text”).
- Keeps the system local, open source, and GPU-accelerated.

---

## 4. References (open source)

- **MLX (Apple):** https://github.com/ml-explore/mlx  
- **mlx-embeddings:** https://github.com/Blaizzy/mlx-embeddings  
- **Ollama:** https://ollama.ai  
- **llama.cpp (Metal):** https://github.com/ggerganov/llama.cpp  
- **ChromaDB:** https://www.trychroma.com/  
- **sentence-transformers:** https://www.sbert.net/  
- **LlamaIndex (local RAG, retrieval-only possible):** https://docs.llamaindex.ai/ (e.g. “Building RAG from Scratch (Open-source only!)”)  
- **HTML / semantic chunking:** Structure-aware chunking by section/heading; your existing IDs and semantics can drive chunk boundaries and metadata.

---

## 5. Summary

- **Best match for “no generative AI”:** **Retrieval-only** pipeline: embed 20k pages (chunked by your HTML structure/IDs), embed queries, vector (+ optional keyword) search, return ranked passages as EN “answers.”
- **Platform:** M2 Mac, GPU via Metal (MLX or MPS), all open source.
- **Optional later step:** Add a small local LLM only to turn retrieved chunks into a single short EN answer, without open-ended generation.

If you want, the next step can be a minimal **aill** ingestion script (HTML → chunks + IDs → embeddings → ChromaDB/FAISS) and a tiny query API that returns EN passages only.
