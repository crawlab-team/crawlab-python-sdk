import os
import re
import sys
from typing import Optional

from httpx import Response
from rich.console import Console

from crawlab.client import http_post
from crawlab.constants.upload import (
    CLI_DEFAULT_UPLOAD_SPIDER_MODE,
    CLI_DEFAULT_UPLOAD_SPIDER_CMD,
    CLI_DEFAULT_UPLOAD_IGNORE_PATTERNS,
)

console = Console()


def create_spider(
    name: str,
    description: Optional[str] = None,
    mode: Optional[str] = None,
    priority: Optional[int] = None,
    cmd: Optional[str] = None,
    param: Optional[str] = None,
    col_name: Optional[str] = None,
) -> Response:
    # results collection name
    if col_name is None:
        col_name = f'results_{"_".join(name.lower().split(" "))}'

    # mode
    if mode is None:
        mode = CLI_DEFAULT_UPLOAD_SPIDER_MODE

    # cmd
    if cmd is None:
        cmd = CLI_DEFAULT_UPLOAD_SPIDER_CMD

    # http post
    return http_post(
        url="/spiders",
        data={
            "name": name,
            "description": description,
            "mode": mode,
            "priority": priority,
            "cmd": cmd,
            "param": param,
            "col_name": col_name,
        },
    )


def upload_file(_id: str, file_path: str, target_path: str) -> Response:
    with open(file_path, "rb") as f:
        data = {
            "path": target_path,
        }
        files = {"file": f}

        url = f"/spiders/{_id}/files/save"
        return http_post(url=url, data=data, files=files, headers={})


def upload_dir(
    dir_path: str,
    create: bool = True,
    spider_id: str = None,
    name=None,
    description=None,
    mode=None,
    priority=None,
    cmd=None,
    param=None,
    col_name=None,
    exclude_path: list = None,
):
    # create spider
    if create:
        response = create_spider(
            name=name,
            description=description,
            mode=mode,
            priority=priority,
            cmd=cmd,
            param=param,
            col_name=col_name,
        )
        if response.status_code != 200:
            console.print(f"[red]create spider {name} failed[/red]")
            sys.exit(1)
        spider_id = response.json().get("data").get("_id")
        console.print(f"[green]created spider {name} (id: {spider_id})[/green]")

    # stats
    stats = {
        "success": 0,
        "error": 0,
    }

    # iterate all files in the directory
    for root, dirs, files in os.walk(dir_path):
        for file_name in files:
            # file path
            file_path = os.path.join(root, file_name)

            # ignored file
            if is_ignored(file_path, exclude_path):
                continue

            # target path
            target_path = file_path.replace(dir_path, "")

            # upload file
            response = upload_file(spider_id, file_path, target_path)
            if response.status_code != 200:
                console.print(f"[red]failed to upload {file_path}[/red]")
                stats["error"] += 1
                continue
            console.print(f"[green]uploaded {file_path}[/green]")
            stats["success"] += 1

    # logging
    console.print(f"[green]uploaded spider {name}[/green]")
    console.print(f"[cyan]success: {stats['success']}[/cyan]")
    console.print(f"[cyan]failed: {stats['error']}[/cyan]")


def is_ignored(file_path: str, exclude_path_patterns: list = None) -> bool:
    exclude_path_patterns = exclude_path_patterns or []
    ignore_patterns = exclude_path_patterns + CLI_DEFAULT_UPLOAD_IGNORE_PATTERNS
    for pat in ignore_patterns:
        if re.search(pat, file_path) is not None:
            return True
    return False
