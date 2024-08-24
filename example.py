from dict2md import dict2md

d = {
    "title": "Example Dictionary",
    "description": "This is a sample dictionary.",
    "items": ["Item 1", "Item 2", "Item 3"],
    "details": {"key1": "value1", "key2": "value2"},
    "custom_object": object(),
}

print(dict2md(d, title_keys=["title"]))
