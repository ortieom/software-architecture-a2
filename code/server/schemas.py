from datetime import datetime

from pydantic import BaseModel, Field


class BasicMsg(BaseModel):
    """
    Common schema for message.
    """
    message: str = Field(str, min_length=2, max_length=4096)


class MsgRequest(BasicMsg):
    pass


class Msg(BasicMsg):
    post_time: datetime
