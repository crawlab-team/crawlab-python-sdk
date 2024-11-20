import os
from typing import Optional


def get_task_id() -> Optional[str]:
    return os.getenv('CRAWLAB_TASK_ID')
