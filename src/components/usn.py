import re
from mrkdwn_analysis import MarkdownAnalyzer
from utilities import get_analyzer
from rich.table import Table
from rich.text import Text
from rich.padding import Padding
from rich.console import Group
from rich.markdown import Markdown


def build(full_md: str) -> Group:

    usn_pattern: str = b'(?s)(###\\s\\*\\*United[^*]*\\*\\*.*?\\n.*?)(?=\\n###\\s\\*\\*|$)'
    usn_match: re.match = re.search(
        usn_pattern, full_md.encode())
    usn_md: str = usn_match.group(1).decode()
    usn_analyzer = get_analyzer(usn_md)

    employer: str = [
        header.get('text')
        for header in usn_analyzer.identify_headers().get('Header')
        if header.get('level') == 3
    ][0]

    roles_pattern = b'(?<=####\\s)([\\s\\S]*?)(?=\n<br>\\s|$)'
    roles: list[MarkdownAnalyzer] = [
        get_analyzer(role.decode()) for role
        in re.findall(roles_pattern, usn_analyzer.text.encode())
    ]

    examples_table: Table = Table(
        title="EXAMPLES", title_justify="left",
        border_style="none", box=None, show_header=False)
    examples_table.add_column(style="blockquote")
    examples_table.add_column(style="bold blue")
    examples_table.add_column()
    for row in usn_analyzer.identify_tables().get('Table')[0].get('rows'):
        examples_table.add_row(
            row[0],
            re.search(b'\\[([^\\]]+)\\]', row[1].encode()).group(1).decode(),
        )

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
        Padding(examples_table, (1, 0, 0, 2))
    )
