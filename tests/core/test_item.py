import json

from crawlab.core.item import save_item


def test_save_item_single(capsys):
    test_item = {"name": "test", "value": 123}
    save_item(test_item)

    capsys_res = capsys.readouterr()
    assert capsys_res.err == ""
    assert capsys_res.out.strip() != ""
    assert capsys_res.out.strip().startswith("{")
    assert capsys_res.out.strip().endswith("}")
    message = json.loads(capsys_res.out)

    assert message["type"] == "data"
    assert message["ipc"] is True
    assert isinstance(message["payload"], list)
    assert len(message["payload"]) == 1
    assert message["payload"][0] == test_item


def test_save_item_multiple(capsys):
    test_items = [{"name": "test1", "value": 123}, {"name": "test2", "value": 456}]
    save_item(*test_items)

    capsys_res = capsys.readouterr()
    message = json.loads(capsys_res.out)

    assert message["type"] == "data"
    assert message["ipc"] is True
    assert isinstance(message["payload"], list)
    assert len(message["payload"]) == 2
    assert message["payload"] == list(test_items)
