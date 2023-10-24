from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter(prefix="/editor")

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
  return templates.TemplateResponse("editor.html", {"request": request})

#@router.post("/save_content/")
#async def save_content(content: dict):
    # Save the content to a database or file
    # content will contain the edited text from the Quill.js editor
    #return {"message": "Content saved successfully"}