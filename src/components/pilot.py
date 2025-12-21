import re
from rich.text import Text
from rich.padding import Padding
from rich.console import Group
from rich.markdown import Markdown
from page_renderer import get_analyzer
from mrkdwn_analysis import MarkdownAnalyzer


def build(full_md: str) -> Group:

    pilot_pattern: str = b'(?s)(###\\s\\*\\*Pilot[^*]*\\*\\*.*?\\n.*?)(?=\\n###\\s\\*\\*|$)'
    pilot_match: re.match = re.search(
        pilot_pattern, full_md.encode())
    pilot_md: str = pilot_match.group(1).decode()
    pilot_analyzer = get_analyzer(pilot_md)

    employer: str = [
        header.get('text')
        for header in pilot_analyzer.identify_headers().get('Header')
        if header.get('level') == 3
    ][0]

    roles_pattern = b'(?<=####\\s)([\\s\\S]*?)(?=\n#+\\s|$)'
    roles: list[MarkdownAnalyzer] = [
        get_analyzer(role.decode()) for role
        in re.findall(roles_pattern, pilot_analyzer.text.encode())
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
