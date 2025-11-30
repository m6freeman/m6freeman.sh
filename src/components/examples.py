from rich.console import Group
from rich.syntax import Syntax
from rich.text import Text
from components import ciat
from components import game_dev
from components import hampton
from components import pilot
from components import usn
from components import web_dev


def build() -> Group:

    title: Text = Text("EXAMPLES", style="title_text")

    most_relevant_syntax: Syntax = Syntax("""
$ mf --serverless_developer aws [dotnet, python] github_actions terraform
$ mf --software_engineer c# dotnet enterprise_solutions
        """, lexer="bash")

    historical_syntax: Syntax = Syntax("""
$ mf --enthusiast
$ mf --game_programmer
$ mf --professional  | grep 'history'
        """, lexer="bash")

    return Group(
        title, "\n",
        most_relevant_syntax, "\n",
        pilot.build(), "\n",
        historical_syntax, "\n",
        ciat.build(), "\n",
        game_dev.build(), "\n",
        usn.build(), "\n",
        web_dev.build(), "\n",
        hampton.build(), "\n",
    )
