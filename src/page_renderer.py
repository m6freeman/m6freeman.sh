from mrkdwn_analysis import MarkdownAnalyzer
from resources import consts
from rich.console import Console
from rich.padding import Padding
from rich.panel import Panel
from rich.theme import Theme
from unittest import mock
import io


def get_analyzer(md_string: str) -> MarkdownAnalyzer:
    dummy_path = "/nonexistent/path/tmp.md"
    fake_file = io.StringIO(md_string)

    def fake_open(path, *args, **kwargs):
        fake_file.seek(0)
        return fake_file

    with mock.patch("builtins.open", new=fake_open):
        analyzer = MarkdownAnalyzer(file_path=dummy_path)

    return analyzer


def build(content_panel: Panel, theme: Theme, output_path: str) -> None:

    console: Console = Console(force_terminal=True, theme=theme)

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
