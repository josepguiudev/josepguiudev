import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import Color, TextColor

#CONSTANTS
MAX_WIDTH = "700px"

class Size(Enum):
    SUPER_SMALL = "0.2em"
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT= "1em"
    BIG="2em"
    MORE_BIG="3em"
    VERY_BIG="4em"

STYLESHEETS=[
    #Aqui podemos importar cualquier css de por ejemplo github
    "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" #El swap nos permitira cargar la página con una fuente predeterminada y luego le aplica la establecida así se carga más rápido
]

BASE_STYLE={
    "font_family":Font.DEFAULT.value,
    "color":TextColor.PRIMARY.value,
    "background":Color.PRIMARY.value,
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "background_color": Color.CONTENT.value,
        "color": TextColor.HEADER.value,
        "white_space": "normal",
        "text_align": "start",
        "_hover": {"background_color": Color.COLOR_HOVER.value}
    },
}

title_style = dict(
    width= "100%",
    padding_top = Size.DEFAULT.value,
    color= TextColor.PRIMARY.value
)

button_title_style = dict(
    font_size = Size.DEFAULT.value,
    color= TextColor.SECONDARY.value
)

button_body_style = dict(
    font_size = Size.DEFAULT.value,
    color= TextColor.PRIMARY.value
)

border_image_foot = dict(
    border_radius="7px 25px",
    border="5px solid",
    border_color=Color.COLOR_HOVER.value
)

body_style_size = dict(
    width= "100%",
    spacing= Size.DEFAULT.value,
    max_width= MAX_WIDTH,
    margin_y= Size.DEFAULT.value,
    padding_x=Size.SMALL.value
)