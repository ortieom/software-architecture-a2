from datetime import datetime
from typing import List

from fastapi import FastAPI

from .schemas import MsgRequest, Msg

app = FastAPI()

# in-memory storage
chat: List[Msg] = []


@app.post("/message/")
async def create_message(msg: MsgRequest) -> bool:
    msg_data = Msg(**msg.model_dump(),
                   post_time=datetime.now())
    chat.append(msg_data)
    return True


@app.get("/messages/", response_model=List[Msg])
async def read_messages():
    return chat


@app.get("/messages/count")
async def count_messages() -> int:
    return len(chat)


@app.get("/ping")
async def healthcheck() -> str:
    return 'pong'
