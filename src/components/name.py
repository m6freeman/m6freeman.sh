from rich.console import Group
from rich.text import Text
from rich.padding import Padding


def build() -> Group:

    return Group(
        Text("NAME", style="title_text"),
        "\n",
        Padding(
            Group(
                Text.assemble(
                    ("matthew_freeman", "bold"),
                    " - software engineer"
                ),
            ), (0, 2)
        ),
    )
