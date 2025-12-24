from components import about_contacts
from components import description
from components import error
from components import examples
from components import game_dev
from components import help as help_page
from components import legend
from components import name
from components import options
from components import quote
from components import see_also
from components import synopsis
from components import usn
from components import web_dev
from rich.console import Group
from rich.padding import Padding
from rich.theme import Theme
from utilities import get_contact_data
import json
import page_renderer


# TODO:
# improve building help page table


with open('src/resources/index.md', 'r', encoding='utf-8') as f:
    full_md: str = f.read()

with open("src/resources/theme.json", "r", encoding="utf-8") as f:
    theme_text: dict[str, str] = json.load(f)
theme: Theme = Theme(theme_text)

contact_data: dict[str, str] = get_contact_data(full_md)

page_renderer.build(
    Group(
        Padding(legend.build(), (1, 0, 0, 0)),
        Padding(about_contacts.build(
            contact_data, "src/resources/quote_ext_bg.txt"), (1, 0, 0, 0)),
        Padding(quote.build("src/resources/quote.txt"), (0, 0, 0, 0)),
    ),
    contact_data,
    theme,
    "dist/index"
)

page_renderer.build(
    Group(
        Padding(name.build(full_md), (1, 0, 0, 0)),
        Padding(synopsis.build(full_md), (2, 0, 0, 0)),
        Padding(description.build(full_md), (2, 0, 0, 0)),
    ),
    contact_data,
    theme,
    "dist/about"
)

page_renderer.build(
    Group(
        Padding(help_page.build(), (1, 0, 0, 0)),
    ),
    contact_data,
    theme,
    "dist/help"
)

page_renderer.build(
    Group(
        Padding(name.build(full_md), (1, 0, 0, 0)),
        Padding(synopsis.build(full_md), (2, 0, 0, 0)),
        Padding(description.build(full_md), (2, 0, 0, 0)),
        Padding(options.build(full_md), (2, 0, 0, 0)),
        Padding(examples.build(full_md), (2, 0, 0, 0)),
        Padding(see_also.build(full_md), (2, 0, 0, 0)),
    ),
    contact_data,
    theme,
    "dist/resume"
)

page_renderer.build(
    Group(Padding(error.build("src/resources/error.txt"), (1, 0))),
    contact_data, theme, "dist/error")

page_renderer.build(
    Group(Padding(game_dev.build(full_md), (1, 0))),
    contact_data, theme, "dist/game_dev")

page_renderer.build(
    Group(Padding(usn.build(full_md), (1, 0))),
    contact_data, theme, "dist/usn")

page_renderer.build(
    Group(Padding(web_dev.build(full_md), (1, 0))),
    contact_data, theme, "dist/web_dev")

page_renderer.build(
    Group(Padding(see_also.build(full_md), (1, 0))),
    contact_data, theme, "dist/see_also"
)
