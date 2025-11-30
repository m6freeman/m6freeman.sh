from resources import consts
from rich.console import Group
from rich.panel import Panel
from rich.table import Table


def build() -> Group:

    contact_table: Table = Table(
        border_style="none", box=None, show_header=False)
    contact_table.add_column("", style="cyan", justify="right")
    contact_table.add_column("", style="dim cyan italic")
    contact_table.add_row("Github:", "github.com/m6freeman")
    contact_table.add_row("Email:", "m6freeman@tuta.io")
    contact_table.add_row("Phone:", "3322690095")
    contact_table.add_row("XMPP:", "hjkl@conversations.im")

    contact_panel: Panel = Panel(
        contact_table,
        box=consts.PANEL_BOX_STYLE,
        subtitle_align="right",
        subtitle="Contact",
        width=consts.TWO_COL_WIDTH + 1
    )

    return Group(
        contact_panel
    )
