import json

from crawlab.core.item import save_item, save_items


def test_save_item_single(capsys):
    test_item = {"name": "test", "value": 123}
    save_item(test_item)

    capsys_res = capsys.readouterr()
    assert capsys_res.err == ""
    assert capsys_res.out != ""
    assert capsys_res.out.startswith("{")
    assert capsys_res.out.endswith("}")
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


def test_save_items(capsys):
    test_items = [
        {"name": "test1", "value": 123},
        {"name": "test2", "value": 456},
        {"name": "test3", "value": 789},
    ]
    save_items(test_items)

    capsys_res = capsys.readouterr()
    message = json.loads(capsys_res.out)

    assert message["type"] == "data"
    assert message["ipc"] is True
    assert isinstance(message["payload"], list)
    assert len(message["payload"]) == 3
    assert message["payload"] == test_items


def test_save_items_empty(capsys):
    save_items([])

    capsys_res = capsys.readouterr()
    message = json.loads(capsys_res.out)

    assert message["type"] == "data"
    assert message["ipc"] is True
    assert isinstance(message["payload"], list)
    assert len(message["payload"]) == 0


def test_save_items_generator(capsys):
    def item_generator():
        yield {"name": "test1", "value": 123}
        yield {"name": "test2", "value": 456}

    save_items(item_generator())

    capsys_res = capsys.readouterr()
    message = json.loads(capsys_res.out)

    assert message["type"] == "data"
    assert message["ipc"] is True
    assert isinstance(message["payload"], list)
    assert len(message["payload"]) == 2
    assert message["payload"] == [
        {"name": "test1", "value": 123},
        {"name": "test2", "value": 456},
    ]
