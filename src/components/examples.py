import re
from rich.console import Group
from rich.syntax import Syntax
from rich.text import Text
from components import ciat
from components import game_dev
from components import hampton
from components import pilot
from components import usn
from components import web_dev
from page_renderer import get_analyzer


def build(full_md: str) -> Group:

    examples_pattern: str = b'(?s)(##\\s*EXAMPLES\\s*\\n.*?)(?=\\n##\\s|$)'
    examples_match: re.match = re.search(
        examples_pattern, full_md.encode())
    examples_md: str = examples_match.group(1).decode()
    examples_analyzer = get_analyzer(examples_md)

    header: str = examples_analyzer.identify_headers()\
        .get('Header')[0].get('text')

    title: Text = Text(header, style="title_text")

    most_relevant_syntax: Syntax = Syntax(f"""
$ {examples_analyzer.identify_inline_code()[0].get('code')}
$ {examples_analyzer.identify_inline_code()[1].get('code')}
        """, lexer="bash", word_wrap=True)

    historical_syntax: Syntax = Syntax(f"""
{'\n'.join("$ " + example_syntax.get('code', "") for example_syntax
           in examples_analyzer.identify_inline_code()[2:])}
        """, lexer="bash")

    return Group(
        title, "\n",
        most_relevant_syntax, "\n",
        pilot.build(full_md), "\n",
        historical_syntax, "\n",
        ciat.build(full_md), "\n",
        game_dev.build(), "\n",
        usn.build(), "\n",
        web_dev.build(), "\n",
        hampton.build(), "\n",
    )
