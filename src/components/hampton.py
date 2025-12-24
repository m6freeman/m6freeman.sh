import re
from utilities import get_analyzer
from rich.text import Text
from rich.padding import Padding
from rich.console import Group
from rich.markdown import Markdown
from mrkdwn_analysis import MarkdownAnalyzer


def build(full_md: str) -> Group:

    hotel_pattern: str = b'(?s)(###\\s\\*\\*Hampton[^*]*\\*\\*.*?\\n.*?)(?=\\n###\\s\\*\\*|$)'
    hotel_match: re.match = re.search(
        hotel_pattern, full_md.encode())
    hotel_md: str = hotel_match.group(1).decode()
    hotel_analyzer = get_analyzer(hotel_md)

    employer: str = [
        header.get('text')
        for header in hotel_analyzer.identify_headers().get('Header')
        if header.get('level') == 3
    ][0]

    roles_pattern = b'(?<=####\\s)([\\s\\S]*?)(?=\n#+\\s|$)'
    roles: list[MarkdownAnalyzer] = [
        get_analyzer(role.decode()) for role
        in re.findall(roles_pattern, hotel_analyzer.text.encode())
    ]

    return Group(
        Padding(Text.assemble(
            (employer.split('*')[2] + " ", "bold"),
            (employer.split('*')[5], "blockquote")), (0, 0, 0, 0)),
        *(
            Padding(
                Group(
                    Text(role.identify_paragraphs().get(
                        'Paragraph')[0], "bold"),
                    Markdown('\n'.join(role.text.splitlines()[1:]))
                ),
                (1, 0, 0, 2))
            for role in roles
        ),
    )
