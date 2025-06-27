# app/main.py
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from .routes import router

app = FastAPI()
app.include_router(router)

@app.get("/", response_class=HTMLResponse)
def home():
    # Build absolute path to index.html
    file_path = os.path.join(os.path.dirname(__file__), "templates", "index.html")
    with open(file_path, "r") as f:
        return f.read()