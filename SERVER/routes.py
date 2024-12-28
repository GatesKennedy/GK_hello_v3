# SERVER/routes.py
from fastapi import Request
from fastapi.responses import HTMLResponse

from SERVER.config import get_app, get_templates
from DATA.data_work import projects_data
from DATA.data_tool import skill_columns, attribute_data

app = get_app()
templates = get_templates()

# HELLO PAGE
# index.html
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "projects": projects_data,
            "skills": skill_columns,
            "attributes": attribute_data
        }
    )

# HISTORY PAGE
# time.html
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "projects": projects_data,
            "skills": skill_columns,
            "attributes": attribute_data
        }
    )

# CONTACT PAGE
# talk.html
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "projects": projects_data,
            "skills": skill_columns,
            "attributes": attribute_data
        }
    )