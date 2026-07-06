import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# Initialize a standard FastAPI wrapper app
app = FastAPI(title="Pathos AI Gateway")

# 1. Serve your custom index.html at the homepage root
@app.get("/", response_class=HTMLResponse)
async def read_index():
    # If index.html is in a subfolder like pathos_root/index.html, 
    # change the path string below to match its location.
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

# 2. Tell your frontend JavaScript where to connect dynamically
# (This acts as a fallback or custom endpoint if needed)
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
