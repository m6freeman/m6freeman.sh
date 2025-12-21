import random
import re
from rich.console import Group
from rich.text import Text
from rich.table import Table
from rich.padding import Padding
from page_renderer import get_analyzer


def build(full_md: str) -> Group:

    synopsis_pattern: str = b'(?s)(##\\s*SYNOPSIS\\s*\\n.*?)(?=\\n##\\s|$)'
    synopsis_match: re.match = re.search(synopsis_pattern, full_md.encode())
    synopsis_md: str = synopsis_match.group(1).decode()
    synopsis_analyzer = get_analyzer(synopsis_md)

    colors = ["blue", "cyan", "green", "white"]
    header: str = synopsis_analyzer.identify_headers().get('Header')[
        0].get('text')

    table: Table = Table(show_header=False, border_style="none", box=None)
    table.add_column()
    table.add_column()
    for inline_code in synopsis_analyzer.identify_inline_code():
        table.add_row(
            Text(inline_code.get('code').split()[0], "bold"),
            Text(" ".join(inline_code.get('code').split()[
                 1:]), colors[random.randrange(len(colors))])
        )

    return Group(
        Text(header, style="title_text"),
        "\n",
        Padding(table, (0, 2))
    )
