import reflex as rx
from enum import Enum
from .fonts import Font
from .colors import Color, TextColor

#CONSTANTS
MAX_WIDTH = "700px"

class Size(Enum):
    SMALL="0.5em"
    DEFAULT= "1em"
    BIG="2em"
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
    }
}