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
import json
import page_renderer


# TODO:
# - source data from markdown in m6freeman.github.io


with open('src/resources/index.md', 'r', encoding='utf-8') as f:
    full_md: str = f.read()

with open("src/resources/theme.json", "r", encoding="utf-8") as f:
    theme_text: dict[str, str] = json.load(f)
theme: Theme = Theme(theme_text)

page_renderer.build(
    Group(
        Padding(legend.build(), (1, 0, 0, 0)),
        Padding(about_contacts.build(
            "src/resources/quote_ext_bg.txt"), (1, 0, 0, 0)),
        Padding(quote.build("src/resources/quote.txt"), (0, 0, 0, 0)),
    ),
    theme,
    "dist/index"
)

page_renderer.build(
    Group(
        Padding(name.build(full_md), (1, 0, 0, 0)),
        Padding(synopsis.build(full_md), (2, 0, 0, 0)),
        Padding(description.build(full_md), (2, 0, 0, 0)),
    ),
    theme,
    "dist/about"
)

page_renderer.build(
    Group(
        Padding(help_page.build(), (1, 0, 0, 0)),
    ),
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
        Padding(see_also.build("src/resources/contacts.json"), (2, 0, 0, 0)),
    ),
    theme,
    "dist/resume"
)

page_renderer.build(
    Group(
        Padding(error.build("src/resources/error.txt"), (1, 0)),
    ), theme, "dist/error")

page_renderer.build(
    Group(Padding(game_dev.build(), (1, 0))), theme, "dist/game_dev")

page_renderer.build(
    Group(Padding(usn.build(), (1, 0))), theme, "dist/usn")

page_renderer.build(
    Group(Padding(web_dev.build(), (1, 0))), theme, "dist/web_dev")

page_renderer.build(
    Group(Padding(
        see_also.build("src/resources/contacts.json"),
        (1, 0))), theme, "dist/see_also"
)
