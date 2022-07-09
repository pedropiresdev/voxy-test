from fastapi import FastAPI, Request, Form, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates/")

CHARS_TO_EXCLUDE = ['.', ',', '!', '?', '"', ';', ':']


def remove_characters(words: list) -> list:
    for word in words:
        if word in CHARS_TO_EXCLUDE:
            words.remove(word)

    return words


@router.get("/counter", response_class=HTMLResponse)
def form_get(request: Request):
    result = "Type or paste a text."
    return templates.TemplateResponse('counter.html', context={'request': request, 'result': result})


@router.post("/words-counter", response_class=HTMLResponse)
def form_counter(request: Request, words: str = Form(...)):
    result = len(remove_characters(words.split()))
    if not result:
        return templates.TemplateResponse('counter.html', context={'request': request, 'result': result, 'text': words, 'is_valid': False})

    return templates.TemplateResponse('counter.html', context={'request': request, 'result': result, 'text': words, "is_valid": True})
