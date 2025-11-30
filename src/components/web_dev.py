from rich.table import Table
from rich.text import Text
from rich.padding import Padding
from rich.console import Group
from rich.markdown import Markdown


def build() -> Group:

    web_developer: Markdown = Markdown("""
**Web Developer**

- Gathered requirements, designed, developed, and remotely administered multiple client websites
- Worked with a team of three developers to provide static and dynamic website solutions using `Drupal`, `Wordpress`, `PHP`, `HTML`, `CSS`, `JS`, and `MySQL`
- Diagnosed production impacting issues within `LAMP (Linux/Apache/MySQL/PHP)` environments such as UI issues, expired certificates, and hosting migration issues

    """)

    examples_table: Table = Table(
        title="EXAMPLES", title_justify="left",
        border_style="none", box=None, show_header=False)
    examples_table.add_column(style="blockquote")
    examples_table.add_column(style="bold blue")
    examples_table.add_column()
    examples_table.add_row("2012", "Stroke of Color, Commercial and Residential Painting Services",
                           "web.archive.org/ mindysstrokeofcolor.com")

    return Group(
        Padding(Text.assemble(
            ("Independent Web Development, Thousand Oaks CA ", "bold"),
            ("2009-2015", "blockquote")
        ), (0, 0, 0, 0)),
        Padding(web_developer, (1, 0, 0, 2)),
        Padding(examples_table, (1, 0, 0, 2))
    )
