import reflex as rx
from .fonts import Font
from .colors import Color, TextColor

STYLESHEETS=[
    #Aqui podemos importar cualquier css de por ejemplo github
    "https://fonts.googleapis.com/css?family=Press+Start+2P&display=swap" #El swap nos permitira cargar la página con una fuente predeterminada y luego le aplica la establecida así se carga más rápido
]

BASE_STYLE={
    "font_family":Font.DEFAULT.value,
    "color":TextColor.PRIMARY.value,
    "background":Color.PRIMARY.value
}