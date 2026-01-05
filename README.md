<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Gemini RAG Chatbot</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 40px;
      background-color: #f9f9f9;
      color: #333;
    }
    h1, h2, h3 {
      color: #2c3e50;
    }
    code, pre {
      background: #eee;
      padding: 6px;
      border-radius: 4px;
    }
    .box {
      background: #ffffff;
      padding: 20px;
      border-radius: 6px;
      box-shadow: 0 0 5px rgba(0,0,0,0.1);
      margin-bottom: 20px;
    }
  </style>
</head>
<body>

  <h1>🚀 Gemini RAG Chatbot</h1>

  <div class="box">
    <p>
      A real-world <strong>Generative AI chatbot</strong> built using 
      <strong>Google Gemini</strong> and 
      <strong>Retrieval-Augmented Generation (RAG)</strong> to answer questions
      from private company documents.
    </p>
  </div>

  <h2>✨ Features</h2>
  <ul>
    <li>LLM-powered responses using Gemini (2.5 Flash)</li>
    <li>Retrieval-Augmented Generation (RAG)</li>
    <li>Local embeddings using Sentence Transformers</li>
    <li>FAISS vector database for semantic search</li>
    <li>Hallucination-controlled answers</li>
    <li>Streamlit-based web interface</li>
  </ul>

  <h2>🧠 Architecture Overview</h2>
  <div class="box">
    <ol>
      <li>Documents are loaded and chunked</li>
      <li>Chunks are converted into embeddings</li>
      <li>Embeddings are stored in FAISS vector database</li>
      <li>User query is embedded and matched semantically</li>
      <li>Relevant chunks are injected into the prompt</li>
      <li>Gemini generates a grounded response</li>
    </ol>
  </div>

  <h2>🛠️ Tech Stack</h2>
  <ul>
    <li>Python</li>
    <li>Google Gemini API</li>
    <li>Sentence-Transformers</li>
    <li>FAISS</li>
    <li>Streamlit</li>
  </ul>

  <h2>▶️ How to Run Locally</h2>

  <div class="box">
    <pre>
pip install -r requirements.txt
    </pre>

    <p>Create a <code>.env</code> file:</p>

    <pre>
GEMINI_API_KEY=your_api_key_here
    </pre>

    <p>Run the application:</p>

    <pre>
python -m streamlit run app.py
    </pre>
  </div>

  <h2>🧪 Sample Questions</h2>
  <ul>
    <li>How many paid leaves do employees get per year?</li>
    <li>What are the office working hours?</li>
    <li>Is work from home allowed?</li>
  </ul>

  <h2>🎯 Interview Relevance</h2>
  <div class="box">
    <p>
      This project demonstrates practical experience in:
    </p>
    <ul>
      <li>LLM + RAG system design</li>
      <li>Vector databases and embeddings</li>
      <li>Prompt engineering and grounding</li>
      <li>Hallucination mitigation</li>
      <li>End-to-end Gen-AI application development</li>
    </ul>
  </div>

  <h2>📌 Note</h2>
  <p>
    API keys are excluded from the repository for security reasons.
  </p>

</body>
</html>
