import re
from rich.console import Group
from rich.text import Text
from rich.padding import Padding
from page_renderer import get_analyzer


def build(full_md: str) -> Group:

    desc_pattern: str = b'(?s)(##\\s*DESCRIPTION\\s*\\n.*?)(?=\\n##\\s|$)'
    desc_match: re.match = re.search(
        desc_pattern, full_md.encode())
    desc_md: str = desc_match.group(1).decode()
    desc_analyzer = get_analyzer(desc_md)

    header: str = desc_analyzer.identify_headers().get('Header')[0].get('text')

    return Group(
        Text(header, style="title_text"),
        "\n",
        Padding(
            Group(
                *(Text(paragraph + '\n\n') for paragraph
                  in desc_analyzer.identify_paragraphs().get('Paragraph'))
            ), (0, 2)
        ),
    )
