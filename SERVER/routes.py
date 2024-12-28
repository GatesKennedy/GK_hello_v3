# SERVER/routes.py
from fastapi import Request
from fastapi.responses import HTMLResponse

from SERVER.config import get_app, get_templates
from DATA.data_work import projects_data
from DATA.data_tool import skill_columns, attribute_data
from DATA.const_strings import STRINGS

app = get_app()
templates = get_templates()
def get_base_context(request: Request) -> dict:
    return {
        "request": request,
        "STRINGS": STRINGS,
        "projects": projects_data,
        "skills": skill_columns,
        "attributes": attribute_data
    }

# HELLO PAGE
# index.html
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "skills": skill_columns,
            "attributes": attribute_data
        }
    )

# HISTORY PAGE
# time.html
@app.get("/time", response_class=HTMLResponse)
async def time(request: Request):
    context = get_base_context(request)
    return templates.TemplateResponse(
        "time.html",
        context
    )

# CONTACT PAGE
# talk.html
@app.get("/talk", response_class=HTMLResponse)
async def talk(request: Request):
    context = get_base_context(request)
    return templates.TemplateResponse("talk.html", context)


# VOID PAGE
# void.html
@app.get("/void", response_class=HTMLResponse)
async def void(request: Request):
    context = get_base_context(request)
    return templates.TemplateResponse("void.html", context)