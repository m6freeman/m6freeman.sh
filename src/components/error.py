from rich.text import Text
from rich.padding import Padding
from rich.console import Group
from resources import consts


def build(error_text_path: str) -> Group:

    with open(error_text_path, "r", encoding="utf-8") as f:
        error_text: str = f.read()

    return Group(
        Text("Well, here I am!", justify="center"),
        Padding(Text(error_text, justify="center"), (2, 0)),
        Text("I knew I should have taken that left turn at Albuquerque.",
             justify="center"),
        "\n",
        Text("$ curl -s m6freeman.sh",
             style="dim", justify="center")
    )
