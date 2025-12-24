from resources import consts
from rich.console import Console
from rich.padding import Padding
from rich.panel import Panel
from rich.theme import Theme


def build(content_panel: Panel, contact_data: dict[str, str],
          theme: Theme, output_path: str) -> None:

    console: Console = Console(force_terminal=True, theme=theme)

    wrapper: Panel = Panel(
        content_panel,
        box=consts.PANEL_BOX_STYLE,
        border_style="cyan",
        subtitle=" - ".join((v for k, v in contact_data.items())),
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
