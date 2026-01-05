from sentence_transformers import SentenceTransformer
import os
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

DOCS_PATH = "docs"
CHUNK_SIZE = 500
OVERLAP = 50

def read_documents():
    texts = []
    for file in os.listdir(DOCS_PATH):
        with open(os.path.join(DOCS_PATH, file), "r", encoding="utf-8") as f:
            texts.append(f.read())
    return texts

def chunk_text(text):
    chunks = []
    for i in range(0, len(text), CHUNK_SIZE - OVERLAP):
        chunks.append(text[i:i+CHUNK_SIZE])
    return chunks

def build_vector_store():
    documents = read_documents()
    chunks = []

    for doc in documents:
        chunks.extend(chunk_text(doc))

    embeddings = model.encode(chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype("float32"))

    return index, chunks
