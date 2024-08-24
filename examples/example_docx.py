# Example usage
from dict2md.dict2docx import dict2docx

d = {
    "title": "Example Dictionary",
    "description": "This is a sample dictionary.",
    "items": ["Item 1", "Item 2", "Item 3"],
    "details": {"key1": "value1", "key2": "value2"},
    "custom_object": object(),
}

dict2docx(d, title_keys=["title"], output_filename="example_word_doc.docx")
