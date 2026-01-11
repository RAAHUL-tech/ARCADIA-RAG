# ARCADIA-RAG  
**Adaptive Retrieval with Critique-Driven Intelligence and Auto-tuning**

ARCADIA-RAG is a production-grade, research-oriented RAG system that dynamically adapts its pipeline per query, critiques and refines its own answers, and continuously optimizes for latency–accuracy tradeoffs.

Unlike traditional RAG pipelines that apply a single static workflow to all queries, ARCADIA-RAG introduces query-aware routing, adaptive chunking, selective self-refinement, and evaluation-driven auto-tuning—all built CPU-only using free-tier resources.

---

## Key Features

- **Query-Adaptive Routing**  
  Dynamically selects chunking strategy, retrieval depth, and inference path based on query intent, complexity, and risk.

- **Advanced Dynamic Chunking**  
  Structural, semantic, and query-aware chunking with adaptive merge/split logic.

- **Hybrid Knowledge Base**  
  Combines vector search (FAISS), sparse retrieval (BM25), metadata filtering, and a lightweight graph layer.

- **Multi-Stage Retrieval & Ranking**  
  Dense and sparse retrieval, reciprocal rank fusion, cross-encoder re-ranking, and diversity-aware scoring.

- **Critique-Augmented Self-Refinement**  
  High-risk or complex queries trigger a critique loop that verifies factuality, coverage, and grounding before refinement.

- **Latency-Optimized Inference (CPU)**  
  Uses vLLM (CPU mode) with paged attention, batching, streaming, and early-exit decoding.

- **Ranking-Aware Confidence Estimation**  
  Final answers include confidence scores derived from ranking margins and critique feedback.

- **Comprehensive RAG Evaluation & Auto-Tuning**  
  Offline evaluation using RAGAS and custom metrics, with Optuna-based parameter tuning.

---

## System Overview

### High-Level Architecture

```
User Query
│
▼
Query Analyzer
(Intent, Complexity, Risk, Latency Sensitivity)
│
▼
Adaptive Pipeline Router
│
├── Simple Query Path ────────────────┐
│                                     │
▼                                     ▼
Dynamic Chunking                     Lightweight Retrieval
│                                     │
▼                                     ▼
Multi-Stage Retrieval               Fast Generation (vLLM)
(Dense + BM25 + Metadata)                  │
│                                     ▼
▼                             Final Answer + Confidence
Fusion & Re-Ranking
│
▼
Draft Answer (vLLM)
│
▼
Critique Engine (Selective)
│
├── High Confidence → Final Answer
│
└── Low Confidence → Targeted Re-Retrieval → Re-Rank → Refined Answer
│
▼
Evaluation & Auto-Tuning Loop
```

---

## Core Components

### 1️⃣ Query Analyzer & Adaptive Router

Each query is classified along multiple dimensions:

- **Intent:** factoid, reasoning, or multi-hop
- **Complexity:** shallow vs deep context requirements
- **Risk:** hallucination sensitivity level
- **Latency sensitivity:** real-time vs offline tolerance

The router decides chunk size, retrieval depth (top-k), whether critique/refinement is enabled, and inference strategy.

### 2️⃣ Advanced Dynamic Chunking

Documents are chunked using a multi-stage process:

- **Structural chunking:** sections, headers, paragraphs
- **Semantic chunking:** embedding similarity shifts
- **Adaptive merging/splitting:** based on query type

This avoids fixed-size chunk limitations and improves retrieval quality.

### 3️⃣ Hybrid Knowledge Base

| Layer | Purpose |
|-------|---------|
| FAISS Vector Store | Semantic retrieval |
| BM25 Index | Lexical precision |
| Metadata Store (SQLite) | Trust, recency, domain |
| Graph Layer | Lightweight entity relations |

Multiple retrieval views improve recall, precision, and grounding.

### 4️⃣ Multi-Stage Retrieval, Fusion & Ranking

Retrieval is compositional:

1. Dense retrieval (FAISS)
2. Sparse retrieval (BM25)
3. Metadata filtering
4. Reciprocal Rank Fusion (RRF)
5. Cross-encoder re-ranking
6. Diversity and trust-aware scoring

### 5️⃣ Critique-Augmented Self-Refinement

For complex or high-risk queries, a critique model evaluates factuality, coverage, and logical consistency. If confidence is low, the system performs targeted re-retrieval instead of a full retry. Context is re-ranked and the answer is refined. Simple queries skip this loop to minimize latency.

### 6️⃣ Latency-Optimized Inference (CPU)

Key optimizations include:

- vLLM (CPU mode)
- Paged attention enabled
- Request batching
- Streaming output
- Early-exit decoding for simple queries

Triton concepts such as kernel fusion and attention memory layout are analyzed and benchmarked theoretically and empirically.

### 7️⃣ Ranking-Aware Confidence Estimation

Final responses include confidence score, evidence coverage, and source diversity. These are computed using ranking margins, critique confidence, and context overlap.

### 8️⃣ RAG Evaluation & Auto-Tuning

#### Evaluation Metrics

- Retrieval recall@k
- Faithfulness
- Context utilization
- Answer correctness
- Latency (p50, p95)
- Token efficiency

#### Auto-Tuning Loop

```
Config → RAG Run → Evaluation → Error Attribution → Parameter Update
```

Using Optuna, the system learns optimal configurations and produces a latency–accuracy Pareto frontier.

---

## Technology Stack

| Layer | Tools |
|-------|-------|
| LLM Inference | vLLM (CPU) |
| External LLMs | Groq, Together (free tier) |
| Embeddings | bge-small, MiniLM |
| Vector DB | FAISS |
| Ranking | Cross-Encoders |
| Orchestration | LangGraph |
| Evaluation | RAGAS |
| Auto-Tuning | Optuna |
| Experiment Tracking | MLflow (local) |
| Storage | SQLite |

---

## Why ARCADIA-RAG Matters

This project demonstrates advanced RAG system design, latency-aware LLM inference, evaluation-driven optimization, and production realism under strict resource constraints. It closely mirrors real-world enterprise RAG systems and research prototypes.

---

## 🤝 Contributing

Contributions are welcome! Please read our contributing guidelines and submit pull requests.

---

## 📄 License

MIT

---

## 📬 Contact

For questions or collaboration opportunities, please open an issue or reach out via email.

---

## 🙏 Acknowledgments

Built with inspiration from recent advances in RAG systems, adaptive inference, and LLM evaluation frameworks.
