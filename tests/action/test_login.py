import os

from crawlab.actions.login import login
from crawlab.constants.upload import (
    CLI_DEFAULT_API_PASSWORD,
    CLI_DEFAULT_API_USERNAME,
)
from crawlab.utils.config import config
from crawlab.utils.request import get_api_address


def test_login():
    login(get_api_address(), CLI_DEFAULT_API_USERNAME, CLI_DEFAULT_API_PASSWORD)
    assert os.path.exists(config.json_path)
    assert len(config.data.get("token")) > 0
