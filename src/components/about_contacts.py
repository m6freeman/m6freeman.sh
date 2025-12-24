from components import about
from components import contacts
from rich.console import Group
from rich.columns import Columns


def build(contact_data: dict[str, str], quote_ext_bg_path: str) -> Group:

    about_panel_group: Group = about.build()
    contacts_panel_group: Group = contacts.build(contact_data)

    with open(quote_ext_bg_path) as f:
        stars_filler_text = f.read()

    about_contact_columns: Columns = Columns([
        about_panel_group,
        Group(
            contacts_panel_group,
            stars_filler_text
        ),
    ])

    return Group(about_contact_columns)
