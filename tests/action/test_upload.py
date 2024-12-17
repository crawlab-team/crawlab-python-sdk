import os
import tempfile
from argparse import Namespace
from datetime import datetime

import httpx
import pytest

from crawlab.cli.login import cli_login
from crawlab.cli.upload import cli_upload
from crawlab.utils.config import config
from crawlab.utils.request import get_api_address


@pytest.fixture
def setup_test_dir():
    name = "test_spider" + f"_{int(datetime.now().timestamp())}"
    dir_path = os.path.join(tempfile.gettempdir(), name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    venv_dir = os.path.join(dir_path, ".venv")
    if not os.path.exists(venv_dir):
        os.makedirs(venv_dir)
    with open(os.path.join(venv_dir, "pyvenv.cfg"), "w") as f:
        f.write("virtualenv = 20.13.0")
    os.chdir(dir_path)
    return name, dir_path


@pytest.fixture
def endpoint():
    return get_api_address()


def test_upload(setup_test_dir, endpoint):
    name, dir_path = setup_test_dir
    with open(os.path.join(dir_path, "main.py"), "w") as f:
        f.write("print('hello world')")
    description = "test_description_" + f"_{int(datetime.now().timestamp())}"
    mode = "random"
    priority = 1
    cmd = "echo hello"
    param = "test"

    cli_login(Namespace(username="admin", password="admin", api_address=endpoint))
    cli_upload(
        Namespace(
            id=None,
            dir=None,
            name=name,
            description=description,
            mode=mode,
            priority=priority,
            cmd=cmd,
            param=param,
            col_name=None,
            create=True,
            exclude_path=".venv",
        )
    )

    res = httpx.get(
        f"{endpoint}/spiders",
        headers={"Authorization": config.data.get("token")},
        params={"size": 1, "page": 1, "sort": "[]"},
    )
    assert res.status_code == 200
    data = res.json().get("data")
    assert len(data) == 1
    spider = data[0]
    assert spider.get("name") == name
    assert spider.get("description") == description
    assert spider.get("mode") == mode
    assert spider.get("cmd") == cmd
    assert spider.get("param") == param

    httpx.delete(
        f'{endpoint}/spiders/{spider.get("_id")}',
        headers={"Authorization": config.data.get("token")},
    )


def test_upload_with_crawlab_json(setup_test_dir, endpoint):
    name, dir_path = setup_test_dir
    description = "test_description_" + f"_{int(datetime.now().timestamp())}"
    mode = "all-nodes"
    priority = 1
    cmd = "echo hello"
    param = "test"

    with open(os.path.join(dir_path, "main.py"), "w") as f:
        f.write("print('hello world')")
    with open(os.path.join(dir_path, "crawlab.json"), "w") as f:
        f.write(
            '{"name":"%s","description":"%s","mode":"%s","priority":%d,"cmd":"%s","param":"%s"}'
            % (name, description, mode, priority, cmd, param)
        )

    cli_login(Namespace(username="admin", password="admin", api_address=endpoint))
    cli_upload(
        Namespace(
            id=None,
            dir=None,
            name=name,
            description=None,
            mode=None,
            priority=None,
            cmd=None,
            param=None,
            col_name=None,
            create=True,
            exclude_path=None,
        )
    )

    res = httpx.get(
        f"{endpoint}/spiders",
        headers={"Authorization": config.data.get("token")},
        params={"size": 1, "page": 1, "sort": "[]"},
    )
    assert res.status_code == 200
    data = res.json().get("data")
    spider = data[0]
    assert spider.get("name") == name
    assert spider.get("description") == description
    assert spider.get("mode") == mode
    assert spider.get("cmd") == cmd
    assert spider.get("param") == param

    httpx.delete(
        f'{endpoint}/spiders/{spider.get("_id")}',
        headers={"Authorization": config.data.get("token")},
    )
