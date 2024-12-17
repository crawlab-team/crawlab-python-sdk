import os
import tempfile
from datetime import datetime

import httpx
import pytest

from crawlab.actions.login import login
from crawlab.actions.upload import upload_dir
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

    login(endpoint, username="admin", password="admin")
    upload_dir(
        name=name,
        dir_path=dir_path,
        description=description,
        mode=mode,
        priority=priority,
        cmd=cmd,
        param=param,
        col_name=None,
        create=True,
        exclude_path=[".venv"],
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
