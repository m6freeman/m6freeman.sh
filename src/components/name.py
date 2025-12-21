import re
from rich.console import Group
from rich.text import Text
from rich.padding import Padding
from rich.markdown import Markdown
from page_renderer import get_analyzer


def build(full_md: str) -> Group:

    name_pattern: str = b'(?s)(##\\s*NAME\\s*\\n.*?)(?=\\n##\\s|$)'
    name_match: re.match = re.search(name_pattern, full_md.encode())
    name_md: str = name_match.group(1).decode()
    name_analyzer = get_analyzer(name_md)

    header: str = name_analyzer.identify_headers().get('Header')[0].get('text')
    title: str = name_analyzer.identify_paragraphs().get('Paragraph')[0]

    return Group(
        Text(header, style="title_text"),
        "\n",
        Padding(
            Group(
                Markdown(title)
            ), (0, 2)
        ),
    )
