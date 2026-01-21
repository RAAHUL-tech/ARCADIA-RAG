from ingestion.pdf_loader import load_pdf

if __name__ == "__main__":
    docs = load_pdf("data/raw/papers/A Systematic Framework for Enterprise Knowledge Retrieval- Leveraging LLM-Generated Metadata to Enhance RAG Systems.pdf")

    print(f"\nLoaded {len(docs)} pages\n")

    first = docs[0]
    print("---- METADATA ----")
    for k, v in first.metadata.items():
        print(f"{k}: {v}")

    print("\n---- TEXT PREVIEW ----")
    print(first.text[:500])
