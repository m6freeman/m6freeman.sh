from rich.console import Group
from rich.text import Text


def build(quote_text_path: str) -> Group:

    with open(quote_text_path, "r", encoding="utf-8") as f:
        quote_text: str = f.read()

    quote: Text = Text(quote_text)

    return Group(
        quote
    )
