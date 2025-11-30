from rich.console import Group
from rich.text import Text
from rich.table import Table
from rich.padding import Padding


def build() -> Group:

    table: Table = Table(show_header=False, border_style="none", box=None)
    table.add_column()
    table.add_column()
    mf: Text = Text("mf", "bold")
    table.add_row(mf, Text(
        "--enthusiast linux [arch debian rhel] neovim ocaml open_source rust", "white"))
    table.add_row(mf, Text(
        "--game_programmer unity [c#]", "cyan"))
    table.add_row(mf, Text(
        "--professional agile confluence infor [fsm ghr ionapi lawson] jira scrum", "blue"))
    table.add_row(mf, Text(
        "--serverless_developer aws [dynamodb ec2 ecr ecs eventbridge lambda [dotnet python] s3 ses sns sqs] docker github_actions terraform", "green"))
    table.add_row(mf, Text(
        "--software_engineer c# dotnet [core framework] git iis_for_windows_server ms_sql_server python", "cyan"))

    return Group(
        Text("SYNOPSIS", style="title_text"),
        "\n",
        Padding(table, (0, 2))
    )
