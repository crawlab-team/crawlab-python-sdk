import sys
from typing import Iterable

from crawlab.entity.ipc_message import IPCMessage


def save_item(*items: dict):
    return save_items(items)


def save_items(items: Iterable[dict]):
    msg = IPCMessage(
        type="data",
        payload=items,
    )
    sys.stdout.write(msg.model_dump_json())
    sys.stdout.flush()
