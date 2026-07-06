import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Pathos AI Gateway")

# Enable CORS so your static website can talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all websites to connect
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, PATCH, etc.
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def read_index():
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
