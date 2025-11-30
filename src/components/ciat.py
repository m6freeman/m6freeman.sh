from rich.text import Text
from rich.padding import Padding
from rich.console import Group


def build() -> Group:

    return Group(
        Padding(Text.assemble(
            ("California Institute of Applied Technology, San Diego CA ", "bold"),
            ("2019-2021", "blockquote")
        ), (0, 0, 0, 0)),
        Padding(Text(
            "Associate’s of Applied Science Degree In Software Development"),
            (1, 0, 0, 2)),
    )
