# app/main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from routes import router

app = FastAPI()
app.include_router(router)

@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r") as f:
        return f.read()
