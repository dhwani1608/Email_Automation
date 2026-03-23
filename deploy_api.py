import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from langserve import add_routes
from src.graph import Workflow
from dotenv import load_dotenv

# Load .env file
load_dotenv()


app = FastAPI(
    title="Gmail Automation",
    version="1.0",
    description="LangGraph backend for the AI Gmail automation workflow",
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

def get_runnable():
    return  Workflow().app

# Fetch LangGraph Automation runnable which generates the workouts
runnable = get_runnable()

# Create the Fast API route to invoke the runnable
add_routes(app, runnable)

@app.get("/", response_class=HTMLResponse)
def root():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Inbox Pal • LangGraph Email Automation</title>
  <style>
    :root {
      --bg: #0f172a;
      --bg-2: #0b1022;
      --accent: #22d3ee;
      --accent-2: #f472b6;
      --text: #e2e8f0;
      --muted: #94a3b8;
      --card: rgba(255, 255, 255, 0.06);
      --border: rgba(255, 255, 255, 0.12);
      --shadow: 0 20px 60px rgba(0, 0, 0, 0.35);
    }

    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: "Space Grotesk", "Segoe UI", system-ui, sans-serif;
      color: var(--text);
      background: radial-gradient(900px 500px at 20% 20%, #1e293b 0%, var(--bg) 60%),
                  radial-gradient(700px 400px at 80% 20%, #1f2937 0%, var(--bg-2) 70%);
      min-height: 100vh;
    }

    .wrap {
      max-width: 980px;
      margin: 0 auto;
      padding: 40px 20px 64px;
    }

    .hero {
      display: grid;
      gap: 20px;
      padding: 28px;
      border: 1px solid var(--border);
      border-radius: 20px;
      background: linear-gradient(135deg, rgba(34, 211, 238, 0.12), rgba(244, 114, 182, 0.08));
      box-shadow: var(--shadow);
      position: relative;
      overflow: hidden;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 12px;
      border-radius: 999px;
      font-size: 12px;
      background: rgba(34, 211, 238, 0.15);
      border: 1px solid rgba(34, 211, 238, 0.3);
      color: #67e8f9;
      width: fit-content;
    }

    h1 {
      margin: 0;
      font-size: 34px;
      letter-spacing: -0.02em;
    }

    p {
      margin: 0;
      color: var(--muted);
      font-size: 15px;
      line-height: 1.6;
    }

    .actions {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      margin-top: 6px;
    }

    .btn {
      text-decoration: none;
      color: #0b1022;
      background: var(--accent);
      padding: 10px 16px;
      border-radius: 12px;
      font-weight: 600;
      border: 1px solid transparent;
      transition: transform 0.15s ease, box-shadow 0.15s ease;
      box-shadow: 0 10px 25px rgba(34, 211, 238, 0.35);
    }

    .btn.secondary {
      background: transparent;
      color: var(--text);
      border: 1px solid var(--border);
      box-shadow: none;
    }

    .btn:hover {
      transform: translateY(-2px);
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 16px;
      margin-top: 22px;
    }

    .card {
      padding: 16px;
      border-radius: 16px;
      background: var(--card);
      border: 1px solid var(--border);
      min-height: 120px;
    }

    .card h3 {
      margin: 0 0 8px 0;
      font-size: 16px;
    }

    .pill {
      display: inline-block;
      padding: 4px 10px;
      font-size: 12px;
      border-radius: 999px;
      background: rgba(244, 114, 182, 0.18);
      color: #f9a8d4;
      border: 1px solid rgba(244, 114, 182, 0.35);
    }

    .footer {
      margin-top: 22px;
      font-size: 12px;
      color: var(--muted);
      display: flex;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 8px;
    }

    .sparkle {
      position: absolute;
      right: -40px;
      top: -40px;
      width: 120px;
      height: 120px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(34,211,238,0.35), rgba(34,211,238,0));
      filter: blur(2px);
    }
  </style>
</head>
<body>
  <div class="wrap">
    <section class="hero">
      <div class="sparkle"></div>
      <div class="badge">Live • Inbox Pal</div>
      <h1>LangGraph Email Automation</h1>
      <p>
        Your AI co-pilot for Gmail. It categorizes, drafts, and verifies replies,
        plus uses RAG to answer product questions. This page is just a tiny
        dashboard so you know the service is awake.
      </p>
      <div class="actions">
        <a class="btn" href="/docs">Open API Docs</a>
        <a class="btn secondary" href="/playground">LangServe Playground</a>
      </div>
      <div class="grid">
        <div class="card">
          <h3>Status</h3>
          <div class="pill">Running</div>
          <p style="margin-top:10px;">API is up on port 8000.</p>
        </div>
        <div class="card">
          <h3>Gmail Auth</h3>
          <div class="pill">Token Ready</div>
          <p style="margin-top:10px;">Using Gmail modify scope.</p>
        </div>
        <div class="card">
          <h3>RAG Index</h3>
          <div class="pill">ChromaDB</div>
          <p style="margin-top:10px;">Built from the `data/` folder.</p>
        </div>
      </div>
      <div class="footer">
        <span>Tip: use /docs to try a run.</span>
        <span>Made by me, powered by LangGraph.</span>
      </div>
    </section>
  </div>
</body>
</html>
"""

def main():
    # Start the API
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
