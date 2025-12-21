import re
from page_renderer import get_analyzer
from rich.text import Text
from rich.padding import Padding
from rich.console import Group


def build(full_md: str) -> Group:

    ciat_pattern: str = b'(?s)(###\\s\\*\\*California[^*]*\\*\\*.*?\\n.*?)(?=\\n###\\s\\*\\*|$)'
    ciat_match: re.match = re.search(
        ciat_pattern, full_md.encode())
    ciat_md: str = ciat_match.group(1).decode()
    ciat_analyzer = get_analyzer(ciat_md)

    school: list[str] = [
        header.get('text')
        for header in ciat_analyzer.identify_headers().get('Header')
        if header.get('level') == 3
    ][0]

    accredidations: list[str] = [
        header.get('text')
        for header in ciat_analyzer.identify_headers().get('Header')
        if header.get('level') == 5
    ]

    return Group(
        Padding(Text.assemble(
            (school.split('*')[2] + " ", "bold"),
            (school.split('*')[5], "blockquote")
        ), (0, 0, 0, 0)),
        *(
            Padding(Text(accred), (1, 0, 0, 2))
            for accred in accredidations
        ),
    )
