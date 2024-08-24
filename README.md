# dict2md - Create a Markdown String from a Dictionary

A function that takes a Python dictionary and returns a markdown formatted string.

If a key is found in parameter `title_keys: List[str] | None`, then its value will be included at the top (#) level.

If a key has a string value, then the key will be converted to a tile and the key will
be put at h2 level (##) and the string value as body.

If a key has a list value then the elements of the list will be printed as a bulleted list.

It a key has a dictionary value then the function will be called recursively, adding one heading level (#) to all headings.


## Example
```
from dict2md import dict2md

d = {
    "title": "Example Dictionary",
    "description": "This is a sample dictionary.",
    "items": ["Item 1", "Item 2", "Item 3"],
    "details": {"key1": "value1", "key2": "value2"},
    "custom_object": object(),
}

print(dict2md(d, title_keys=["title"]))
```

Which returns:

```
# Example Dictionary

## Description

This is a sample dictionary.

## Items

* Item 1
* Item 2
* Item 3

## Details

### Key1

value1

### Key2

value2

## Custom Object

<object object at 0x1008d5690>
```

Which renders as:

> # Example Dictionary
> 
> ## Description
> 
> This is a sample dictionary.
> 
> ## Items
> 
> * Item 1
> * Item 2
> * Item 3
> 
> ## Details
> 
> ### Key1
> 
> value1
> 
> ### Key2
> 
> value2
> 
> ## Custom Object
> 
> <object object at 0x1008d5690>



# dict2docx - Create a Word File from a Dictionary

There is also a function `dict2docx` that uses `python-docx` to do a similar conversion but saves the result as a Word .docx file.

Use this as follows:

```
from dict2md.dict2docx import dict2docx

d = {
    "title": "Example Dictionary",
    "description": "This is a sample dictionary.",
    "items": ["Item 1", "Item 2", "Item 3"],
    "details": {"key1": "value1", "key2": "value2"},
    "custom_object": object(),
}

dict2docx(d, title_keys=["title"], output_filename="example_word_doc.docx")
```

This will write the file `example_word_doc.docx`
