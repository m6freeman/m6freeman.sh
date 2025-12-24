from resources import consts
from rich.text import Text
from rich.console import Group
from rich.panel import Panel
from rich.table import Table


def build() -> Group:

    legend_table: Table = Table(
        collapse_padding=True,
        border_style="none", box=None, show_header=False, expand=True)
    legend_table.add_column("", style="green", justify="left", width=2)
    legend_table.add_column("", style="dim", justify="left")
    legend_table.add_column("", width=16)
    legend_table.add_column("", style="dim italic", justify="right", width=10)
    legend_table.add_row("$ curl", "-s", "m6freeman.sh",
                         Text("\u25B6 you are here \u25C0", "cyan bold"))
    legend_table.add_row(
        "$ curl", "-s", "m6freeman.sh/about", "a brief summary")
    legend_table.add_row("$ curl", "-s", "m6freeman.sh/help",
                         "full listing of pages")
    legend_table.add_row(
        "$ curl", "-s", "m6freeman.sh/resume | less -r", "the man page")

    legend_panel: Panel = Panel(
        legend_table,
        box=consts.PANEL_BOX_STYLE,
        title_align="left",
        title="Legend",
        width=consts.ONE_COL_WIDTH
    )

    return Group(
        legend_panel,
    )
