import re
import rich.box
from utilities import get_analyzer
from rich.console import Group
from rich.table import Table
from rich.text import Text


def build(full_md: str) -> Group:

    refs_pattern: str = b'(?s)(##\\s*SEE\\sALSO\\s*\\n.*?)(?=\\n##\\s|$)'
    refs_match: re.match = re.search(
        refs_pattern, full_md.encode())
    refs_md: str = refs_match.group(1).decode()
    refs_analyzer = get_analyzer(refs_md)

    header: str = refs_analyzer.identify_headers()\
        .get('Header')[0].get('text')

    t: Table = Table(box=rich.box.SIMPLE_HEAD)
    col_headers: list[str] = refs_analyzer.identify_tables().get('Table')[
        0].get('header')
    t.add_column(col_headers[0], justify="left", style="blue", width=8)
    t.add_column(col_headers[1], justify="left", width=8)
    t.add_column(col_headers[2], justify="left")
    t.add_column(col_headers[3], justify="right", style="blue")
    t.add_column(col_headers[4], justify="right", style="blue")
    for row in refs_analyzer.identify_tables().get('Table')[0].get('rows'):
        try:
            emp: str = re.search(b'\\[([^\\]]+)\\]',
                                 row[0].encode()).group(1).decode()
        except Exception:
            emp = ""
        role: str = row[1] or ""
        name: str = row[2] or ""
        try:
            phone: str = re.search(
                b'\\[([^\\]]+)\\]', row[3].encode()).group(1).decode()
        except Exception:
            phone = ""
        try:
            email: str = re.search(b'\\[([^\\]]+)\\]', row[4].encode()
                                   ).group(1).decode().replace('@', '\n@')
        except Exception:
            email = ""
        t.add_row(emp, role, name, phone, email)
        t.add_row()
    professional_references_table: Table = t

    return Group(
        Text(header, style="title_text"),
        "\n",
        professional_references_table
    )
