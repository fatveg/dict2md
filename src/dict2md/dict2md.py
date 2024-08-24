from typing import Any, Dict, List, Optional


def title_clean(key: str) -> str:
    """
    Clean and format a key to be used as a title.

    :param key: The key to clean.
    :return: A cleaned and formatted title.
    """
    return key.replace("_", " ").title()


def dict2md(
    d: Dict[str, Any], title_keys: Optional[List[str]] = None, heading_level: int = 1
) -> str:
    """
    Convert a dictionary to a markdown formatted string.

    :param d: The dictionary to convert.
    :param title_keys: A list of keys to include at the top (#) level.
    :param heading_level: The current heading level (default=1).
    :return: A markdown formatted string.
    """
    md = ""
    for key, value in d.items():
        if title_keys and key.casefold() in (k.casefold() for k in title_keys):
            md += f"# {value}\n\n"
        elif isinstance(value, str):
            md += f"{'#' * (heading_level + 1)} {title_clean(key)}\n\n{value}\n\n"
        elif isinstance(value, list):
            md += f"{'#' * (heading_level + 1)} {title_clean(key)}\n\n"
            for item in value:
                md += f"* {item}\n"
            md += "\n"
        elif isinstance(value, dict):
            md += f"{'#' * (heading_level + 1)} {title_clean(key)}\n\n"
            md += dict2md(value, title_keys, heading_level + 1)
        else:
            md += f"{'#' * (heading_level + 1)} {title_clean(key)}\n\n{str(value)}\n\n"
    return md
