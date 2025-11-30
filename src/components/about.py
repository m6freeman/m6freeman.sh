from resources import consts
from rich.console import Group
from rich.panel import Panel
from rich.text import Text


def build() -> Group:

    about_panel: Panel = Panel(
        Text(
            """Hey, I'm Matt and this is my attempt at a unique resume.

You can find out more about me, my past experience and projects, or just a few things I find interesting by following the legend above.""",
            justify="left",
        ),
        title="About",
        box=consts.PANEL_BOX_STYLE,
        title_align="left",
        width=consts.TWO_COL_WIDTH - 2
    )

    return Group(
        about_panel
    )
