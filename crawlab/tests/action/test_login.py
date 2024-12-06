import os
from argparse import Namespace

from crawlab.cli.login import cli_login
from crawlab.utils.config import config
from crawlab.utils.request import get_api_address


def test_login():
    args = Namespace(
        username="admin",
        password="admin",
        api_address=get_api_address(),
    )
    cli_login(args)
    assert os.path.exists(config.json_path)
    assert len(config.data.get("token")) > 0
