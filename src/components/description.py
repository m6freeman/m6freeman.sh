from rich.console import Group
from rich.text import Text
from rich.padding import Padding


def build() -> Group:

    return Group(
        Text("DESCRIPTION", style="title_text"),
        "\n",
        Padding(
            Group(
                Text("Actively develops event-driven, serverless enterprise solutions while supporting legacy corporate infrastructure."),
                "\n",
                Text(
                    "Strong technical background encompassing a variety of software and hardware technologies")
            ), (0, 2)
        ),
    )
