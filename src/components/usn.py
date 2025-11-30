from rich.table import Table
from rich.text import Text
from rich.padding import Padding
from rich.console import Group
from rich.markdown import Markdown


def build() -> Group:

    mc3: Markdown = Markdown("""

**Mass Communication Specialist 3rd Class (SW)**

- Photographed, filmed, journal/documented, published, and assisted in the coordination of various military operations, events and ceremonies, earning an Admiral's Letter of Commendation for my work during my 2018-19 Western Pacific deployment aboard USS Essex (LHD-2) 
- Designed publications and filmed/edited videos for military promotional use utilizing `Adobe Photoshop`, `InDesign`, and `Premiere`
- Secret Clearance eligible

    """)

    examples_table: Table = Table(
        title="EXAMPLES", title_justify="left",
        border_style="none", box=None, show_header=False)
    examples_table.add_column(style="blockquote")
    examples_table.add_column(style="bold blue")
    examples_table.add_column()
    examples_table.add_row("2018", "USS Essex Westpac",
                           "github.com/m6freeman/uss_essex_photos")

    return Group(
        Padding(Text.assemble(
            ("United States Navy, San Diego CA ", "bold"),
            ("2015-2019", "blockquote")
        ), (0, 0, 0, 0)),
        Padding(mc3, (1, 0, 0, 2)),
        Padding(examples_table, (1, 0, 0, 2))
    )
