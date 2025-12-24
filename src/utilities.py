from mrkdwn_analysis import MarkdownAnalyzer
from unittest import mock
import io
import re


def get_analyzer(md_string: str) -> MarkdownAnalyzer:
    dummy_path = "/nonexistent/path/tmp.md"
    fake_file = io.StringIO(md_string)

    def fake_open(path, *args, **kwargs):
        fake_file.seek(0)
        return fake_file

    with mock.patch("builtins.open", new=fake_open):
        analyzer = MarkdownAnalyzer(file_path=dummy_path)

    return analyzer


def get_contact_data(full_md: str) -> dict[str, str]:

    contact_data: dict[str, str] = {}
    contact_pattern: str = b'(?s)(###\\sContact\\sInformation[^*]*.*?\\n.*?)(?=\\n#+\\s*|$)'
    contact_match: re.match = re.search(
        contact_pattern, full_md.encode())
    contact_md: str = contact_match.group(1).decode()
    contact_analyzer = get_analyzer(contact_md)
    table = contact_analyzer.identify_tables().get('Table')[0]
    contact_type: list[str] = table.get('header')
    for header, row in zip(contact_type, table.get('rows')[0]):
        contact_data.update(
            {
                header: re.search(
                    b'\\[([^\\]]+)\\]', row.encode()).group(1).decode()
            })

    return contact_data
