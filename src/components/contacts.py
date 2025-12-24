import re
from page_renderer import get_analyzer
from resources import consts
from rich.console import Group
from rich.panel import Panel
from rich.table import Table


def build(contact_data: dict[str, str]) -> Group:

    contact_table: Table = Table(
        border_style="none", box=None, show_header=False)
    contact_table.add_column("", style="cyan", justify="right")
    contact_table.add_column("", style="dim cyan italic")
    contact_table.add_row("Github:", "github.com/m6freeman")
    for k, v in contact_data.items():
        contact_table.add_row(k, v)

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
