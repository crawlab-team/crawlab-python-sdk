import os
import re
from typing import Optional


def get_task_id() -> Optional[str]:
    task_id = os.getenv("CRAWLAB_TASK_ID")

    # Only allow ObjectId format
    if task_id and re.match(r"^[a-fA-F0-9]{24}$", task_id):
        return task_id
    else:
        return None
