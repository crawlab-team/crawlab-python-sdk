from typing import Iterable, Literal, Optional

from pydantic import BaseModel, Field


class IPCMessage(BaseModel):
    type: Optional[Literal["data", "log"]] = Field(description="Message type")
    ipc: bool = Field(description="The message is IPC", default=True)
    payload: Iterable[dict] | dict = Field(description="Message payload")
