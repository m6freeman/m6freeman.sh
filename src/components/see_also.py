import json
import rich.box
from rich.console import Group
from rich.table import Table
from rich.text import Text


def build(contacts_path: str) -> Group:

    with open(contacts_path, "r", encoding="utf-8") as f:
        contacts: list[dict[str, str]] = json.load(f)

    t: Table = Table(box=rich.box.SIMPLE_HEAD)
    t.add_column("Employer", justify="left", style="blue", width=8)
    t.add_column("Role", justify="left", width=8)
    t.add_column("Name", justify="left")
    t.add_column("Phone", justify="right", style="blue")
    t.add_column("Email", justify="right", style="blue")
    for contact in contacts:
        t.add_row(
            contact.get("employer", ""),
            contact.get("role", ""),
            contact.get("name", ""),
            contact.get("phone", ""),
            contact.get("email", "")
        )
        t.add_row()
    professional_references_table: Table = t

    return Group(
        Text("SEE ALSO", style="title_text"),
        "\n",
        professional_references_table
    )
