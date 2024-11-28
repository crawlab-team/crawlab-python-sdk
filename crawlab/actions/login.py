from crawlab.constants.upload import (
    CLI_DEFAULT_CONFIG_KEY_API_ADDRESS,
    CLI_DEFAULT_CONFIG_KEY_PASSWORD,
    CLI_DEFAULT_CONFIG_KEY_TOKEN,
    CLI_DEFAULT_CONFIG_KEY_USERNAME,
)
from crawlab.utils.config import config
from crawlab.utils.request import http_post


def login(api_address: str, username: str, password: str):
    url = f"{api_address}/login"
    try:
        res = http_post(
            url,
            {
                "username": username,
                "password": password,
            },
        )
        print("logged-in successfully")
    except Exception as e:
        print(e)
        return

    token = res.json().get("data")
    config.set(CLI_DEFAULT_CONFIG_KEY_USERNAME, username)
    config.set(CLI_DEFAULT_CONFIG_KEY_PASSWORD, password)
    config.set(CLI_DEFAULT_CONFIG_KEY_API_ADDRESS, api_address)
    config.set(CLI_DEFAULT_CONFIG_KEY_TOKEN, token)
    config.save()
