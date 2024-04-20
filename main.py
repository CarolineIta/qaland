from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from open_ai import send_chat_to_openai

app = FastAPI()

app.mount("/static", StaticFiles(directory="templates/static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("create_chart.html", {"request": request})

@app.get("/chat", response_class=HTMLResponse)
def send_chat():

    response = send_chat_to_openai("Quando eu falar 'Hey', você diz 'How'", "Hey!")
    return response