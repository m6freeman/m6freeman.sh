from resources import consts
from rich.text import Text
from rich.console import Group
from rich.panel import Panel
from rich.table import Table


def build() -> Group:

    help_table: Table = Table(
        border_style="none", box=None, show_header=False, expand=True)
    help_table.add_column("", style="green", justify="right")
    help_table.add_column("", style="dim", justify="left")
    help_table.add_column()
    help_table.add_column("", style="dim italic", justify="right")
    help_table.add_row()
    help_table.add_row("$ curl", "-s", "m6freeman.sh", "welcome page")
    help_table.add_row("$ curl", "-s", "m6freeman.sh/about", "a brief summary")
    help_table.add_row(
        "$ curl", "-s", "m6freeman.sh/game_dev", "indie game dev stuff")
    help_table.add_row("$ curl", "-s", "m6freeman.sh/help",
                       Text("\u25B6  you are here \u25C0", "cyan bold"))
    help_table.add_row("$ curl", "-s", "m6freeman.sh/pilot",
                       "current employment")
    help_table.add_row(
        "$ curl", "-s", "m6freeman.sh/resume | less -r", "the man page")
    help_table.add_row("$ curl", "-s", "m6freeman.sh/see_also",
                       "professional references")
    help_table.add_row("$ curl", "-s", "m6freeman.sh/usn",
                       "my time in the navy")
    help_table.add_row(
        "$ curl", "-s", "m6freeman.sh/web_dev", "humble beginnings")
    help_table.add_row()

    help_panel: Panel = Panel(
        help_table,
        box=consts.PANEL_BOX_STYLE,
        title_align="left",
        title="Help",
        width=consts.ONE_COL_WIDTH
    )

    return Group(
        help_panel,
    )
