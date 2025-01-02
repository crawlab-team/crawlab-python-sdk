import sys

from crawlab.entity.ipc_message import IPCMessage


def save_item(*items: dict):
    msg = IPCMessage(
        type="data",
        payload=items,
    )
    sys.stdout.write(msg.model_dump_json() + "\n")
    sys.stdout.flush()
