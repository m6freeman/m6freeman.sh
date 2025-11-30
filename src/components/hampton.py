from rich.table import Table
from rich.text import Text
from rich.padding import Padding
from rich.console import Group
from rich.markdown import Markdown


def build() -> Group:

    guest_services: Markdown = Markdown("""

**Guest Services Assistant**

- Managed room inventory through POS application
- Trained new employees on POS applications and hotel policies
- Performed on-call maintenance to computers and room appliances

    """)

    return Group(
        Padding(Text.assemble(
            ("Hampton Inn, Agoura Hills CA ", "bold"),
            ("2008-2015", "blockquote")
        ), (0, 0, 0, 0)),
        Padding(guest_services, (1, 0, 0, 2)),
    )
