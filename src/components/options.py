import re
from rich.console import Group
from rich.panel import Panel
from rich.padding import Padding
from rich.text import Text
from utilities import get_analyzer
import rich.box


def build(full_md: str) -> Group:

    options_pattern: str = b'(?s)(##\\s*OPTIONS\\s*\\n.*?)(?=\\n##\\s|$)'
    options_match: re.match = re.search(
        options_pattern, full_md.encode())
    options_md: str = options_match.group(1).decode()
    options_analyzer = get_analyzer(options_md)

    header: str = options_analyzer.identify_headers()\
        .get('Header')[0].get('text')

    options: list[str] = [
        code.get('code') for code
        in options_analyzer.identify_inline_code()
        if code.get('code').startswith('--')
    ]

    techs: list[str] = [
        code.get('code') for code
        in options_analyzer.identify_inline_code()
        if not code.get('code').startswith('--')
    ]

    blockquotes: list[str] = [
        Padding(Text.assemble(
            *((word, "cyan") if word in techs else word
                for word in blockquote.split('`')),
            style="blockquote"), (0, 4))
        for blockquote in
        options_analyzer.identify_blockquotes().get('Blockquote')
    ]

    return Group(
        Text(header, style="title_text"),
        "\n",
        *(
            text_or_panel
            for option, blockquote in zip(options, blockquotes)
            for text_or_panel in [
                Text(option, style="bold"),
                Panel(blockquote, box=rich.box.SIMPLE, border_style="none")
            ]
        ),
    )
