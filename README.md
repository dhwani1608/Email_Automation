# LangGraph Email Automation (Gmail + RAG)

This is my end-to-end email automation project built with LangGraph and LangChain. It monitors a Gmail inbox, categorizes incoming emails, drafts responses, and uses RAG to answer product/service questions.

I built it to save time on repetitive support emails while keeping responses accurate and consistent.

## What it does
- Watches a Gmail inbox and pulls recent messages
- Categorizes emails (complaint, inquiry, feedback, unrelated)
- Uses RAG to answer product/service questions from my knowledge base
- Drafts and verifies replies before sending

## Tech stack
- Python
- LangGraph + LangChain
- ChromaDB (vector store)
- Gmail API
- Groq + Gemini (LLM + embeddings)
- FastAPI + LangServe for API deployment

## Project structure
- `main.py` runs the workflow
- `deploy_api.py` runs the API server
- `create_index.py` builds the vector store from `data/`
- `src/` contains the graph, agents, nodes, and tools

## Setup
1. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   venv\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root:
   ```env
   MY_EMAIL=your_email@gmail.com
   GROQ_API_KEY=your_groq_api_key
   GOOGLE_API_KEY=your_gemini_api_key
   ```

4. Enable Gmail API and add OAuth credentials:
   - Create a Google Cloud project
   - Enable Gmail API
   - Create **Desktop App** OAuth client
   - Save it as `credentials.json` in the project root

5. Build the vector index (optional, if you add new docs):
   ```powershell
   python create_index.py
   ```

## Run the workflow
```powershell
venv\Scripts\python.exe main.py
```

The first run will open a browser to authorize Gmail and create `token.json`.

## Run as an API
```powershell
venv\Scripts\python.exe deploy_api.py
```

Then open:
- `http://localhost:8000/docs` for Swagger UI
- `http://localhost:8000/openapi.json` for the schema

## Notes
- `0.0.0.0` is a bind address, use `localhost` in the browser.
- If you see OAuth errors, make sure the consent screen is External and you’re added as a test user.

## Customize
- Update prompts and logic in `src/`
- Add your docs in `data/` and rebuild the index

## Why I built this
I wanted a practical, production-like email assistant that combines smart routing, retrieval, and clean drafting. This repo is my working version of that idea.
