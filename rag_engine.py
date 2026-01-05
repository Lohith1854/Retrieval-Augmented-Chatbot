import os
import numpy as np
from dotenv import load_dotenv
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
from embed_store import build_vector_store

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Local embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Lazy-loaded vector store
_index = None
_chunks = None

def init_store():
    global _index, _chunks
    if _index is None:
        _index, _chunks = build_vector_store()

def retrieve_context(query, k=3):
    init_store()
    query_vec = embed_model.encode([query])
    _, indices = _index.search(np.array(query_vec).astype("float32"), k)
    return "\n\n".join([_chunks[i] for i in indices[0]])

def generate_answer(question):
    context = retrieve_context(question)

    prompt = f"""
You are a company assistant.
Answer ONLY using the context below.
If the answer is not found, say "Not available".

Context:
{context}

Question:
{question}
"""

    model = genai.GenerativeModel("gemini-2.5-flash")

    response = model.generate_content(prompt)

    return response.text
