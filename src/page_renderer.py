from rich.console import Console
from rich.panel import Panel
from rich.padding import Padding
from rich.theme import Theme
from resources import consts


def build(content_panel: Panel, theme: Theme, output_path: str) -> None:

    console: Console = Console(theme=theme)

    wrapper: Panel = Panel(
        content_panel,
        box=consts.PANEL_BOX_STYLE,
        border_style="cyan",
        subtitle="m6freeman@tuta.io - 3322690095 - hjkl@conversations.im",
        subtitle_align="right",
        title="matthew_freeman(1) - software engineer",
        title_align="left",
        width=consts.MAX_WIDTH
    )
    wrapper: Padding = Padding(wrapper, (1, 2))

    with console.capture() as capture:
        console.print(wrapper)

    with open(output_path, "w") as f:
        f.write(capture.get())
