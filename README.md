<h1>Gemini RAG Chatbot – Retrieval Augmented Generative AI System</h1>

<p>
This project is a real-world <b>Generative AI chatbot</b> built using 
<b>Google Gemini</b> and <b>Retrieval-Augmented Generation (RAG)</b>.
It enables users to ask natural-language questions over private company documents
and receive accurate, grounded, and hallucination-controlled answers.
</p>

<hr>

<h2>🚀 Features Implemented</h2>
<ul>
  <li>LLM-powered responses using <b>Gemini (2.5 Flash)</b></li>
  <li>Retrieval-Augmented Generation (RAG) architecture</li>
  <li>Local embeddings using <b>Sentence Transformers</b></li>
  <li>FAISS vector database for semantic similarity search</li>
  <li>Context-grounded responses to reduce hallucinations</li>
  <li>Streamlit-based interactive chatbot interface</li>
  <li>Secure API key management using environment variables</li>
</ul>

<hr>

<h2>🛠 How to Run the Project</h2>

<ol>
  <li>
    Create and activate a virtual environment (Windows):<br><br>
    <pre>
python -m venv venv
.\venv\Scripts\Activate.ps1
    </pre>
  </li>

  <li>
    Install dependencies:<br><br>
    <pre>
pip install -r requirements.txt
    </pre>
  </li>

  <li>
    Create a <code>.env</code> file in the project root:<br><br>
    <pre>
GEMINI_API_KEY=your_gemini_api_key_here
    </pre>
  </li>

  <li>
    Run the application:<br><br>
    <pre>
python -m streamlit run app.py
    </pre>
  </li>
</ol>

<hr>

<h2>🧠 RAG Pipeline Overview</h2>

<div class="box">
  <ol>
    <li>Documents are loaded from the <code>docs/</code> directory</li>
    <li>Text is split into overlapping chunks</li>
    <li>Chunks are embedded using a local embedding model</li>
    <li>Embeddings are stored in a FAISS vector database</li>
    <li>User query is embedded and matched semantically</li>
    <li>Top-K relevant chunks are retrieved</li>
    <li>Retrieved context is injected into the Gemini prompt</li>
    <li>Gemini generates a grounded response</li>
  </ol>
</div>

<hr>

<h2>🧪 Sample Questions</h2>
<ul>
  <li>How many paid leaves do employees get per year?</li>
  <li>What are the office working hours?</li>
  <li>Is work from home allowed?</li>
</ul>

<p>
If a question is outside the document scope, the chatbot safely responds with
<b>"Not available"</b> to prevent hallucinations.
</p>

<hr>

<h2>📂 Project Structure</h2>

<pre>
rag-chatbot/
│
├── app.py
├── rag_engine.py
├── embed_store.py
├── docs/
│   ├── hr_policy.txt
│   └── company_faq.txt
├── requirements.txt
├── README.html
</pre>

<hr>

<h2>🔧 Possible Improvements</h2>
<ul>
  <li>Add source citations for answers</li>
  <li>Enable document upload through UI</li>
  <li>Add conversational memory</li>
  <li>Deploy on cloud platforms (AWS / GCP)</li>
  <li>Add authentication and access control</li>
</ul>

<hr>

<h2>👤 Author</h2>
<p>
<b>Narayana Lohith</b><br>
Built as a practical Gen-AI project demonstrating LLM + RAG system design.
</p>

</body>
</html>
