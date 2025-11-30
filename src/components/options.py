from rich.console import Group
from rich.panel import Panel
from rich.padding import Padding
from rich.text import Text
import rich.box


def build() -> Group:

    enthusiast_bq: Text = Text.assemble(
        "Enthusiastic about technologies with a heavy emphasis towards \
privacy, security, transparency, and decentralization.", style="blockquote")
    enthusiast_bq: Padding = Padding(
        enthusiast_bq, (0, 4))

    game_programmer_bq: Text = Text.assemble(
        "Developed and published Android and Windows platform games with ",
        ("Unity3D", "cyan"), ", ",
        ("C#", "cyan"), ", ",
        (".NET Framework", "cyan"), ", and ",
        ("Visual Studio", "cyan"),
        style="blockquote"
    )
    game_programmer_bq: Padding = Padding(
        game_programmer_bq, (0, 4))

    professional_bq: Text = Text.assemble(
        "Collaborates with all levels of personnel, senior leadership, \
and clients to foster continuous improvement and enhance profitability.",
        style="blockquote")
    professional_bq: Padding = Padding(professional_bq, (0, 4))

    serverless_developer_bq: Text = Text.assemble(
        "Designs, develops, and deploys scalable enterprise solutions within ",
        ("AWS", "cyan"), " using ",
        ("API Gateway", "cyan"), ", ",
        ("DynamoDb", "cyan"), ", ",
        ("EC2", ""), ", ",
        ("Lambda", "cyan"), ", ",
        ("S3", "cyan"), ", ",
        ("SNS", "cyan"), ", and ",
        ("SQS", "cyan"),
        style="blockquote"
    )
    serverless_developer_bq: Padding = Padding(
        serverless_developer_bq, (0, 4))

    software_engineer_bq: Text = Text.assemble(
        "Introduce new and modify existing features, perform debugging and \
patching, and perform project and infrastructural upgrades to legacy \
enterprise Financial, Payroll, HR, and Benefits systems", style="blockquote")
    software_engineer_bq: Padding = Padding(software_engineer_bq, (0, 4))

    return Group(
        Text("OPTIONS", style="title_text"),
        "\n",
        Text("--enthusiast", style="bold"),
        Panel(professional_bq, box=rich.box.SIMPLE, border_style="none"),
        Text("--game_programmer", style="bold"),
        Panel(game_programmer_bq, box=rich.box.SIMPLE, border_style="none"),
        Text("--professional", style="bold"),
        Panel(professional_bq, box=rich.box.SIMPLE, border_style="none"),
        Text("--serverless_developer", style="bold"),
        Panel(serverless_developer_bq,
              box=rich.box.SIMPLE, border_style="none"),
        Text("--software_engineer", style="bold"),
        Panel(software_engineer_bq, box=rich.box.SIMPLE, border_style="none"),
    )
