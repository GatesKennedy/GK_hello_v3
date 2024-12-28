# SERVER/config.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Initialize FastAPI app
app = FastAPI(
    title="GK Hello",
    description="Gates Kennedy Portfolio Site",
    version="3.0.0"
)

# static files and templates
app.mount("/static", StaticFiles(directory="STATIC"), name="static")
templates = Jinja2Templates(directory="PLATES")

# app instance
def get_app() -> FastAPI:
    return app

# templates
def get_templates() -> Jinja2Templates:
    return templates