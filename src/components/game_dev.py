from rich.table import Table
from rich.text import Text
from rich.padding import Padding
from rich.console import Group
from rich.markdown import Markdown


def build() -> Group:

    lead_programmer: Markdown = Markdown("""
**Lead Programmer, Owner**

- Developed and published `Android` and `Windows` platform games with `Unity3D`, `C#`, `.NET Framework`, and `Visual Studio`
- Worked directly alongside UI/UX designers and 3D asset animators.

    """)

    examples_table: Table = Table(
        title="EXAMPLES", title_justify="left",
        border_style="none", box=None, show_header=False)
    examples_table.add_column(style="blockquote")
    examples_table.add_column(style="bold blue")
    examples_table.add_column()
    examples_table.add_row(
        "2019", "Subtractor", "github.com/m6freeman/subtractor"
    )
    examples_table.add_row(
        "2016", "Hyperlane", "github.com/m6freeman/hyperlane"
    )
    examples_table.add_row(
        "2015", "Porthole", "github.com/m6freeman/porthole"
    )

    return Group(
        Padding(Text.assemble(
            ("Whale Fall Studios, San Diego CA ", "bold"),
            ("2015-2020", "blockquote")
        ), (0, 0, 0, 0)),
        Padding(lead_programmer, (1, 0, 0, 2)),
        Padding(examples_table, (1, 0, 0, 2))
    )
