import reflex as rx
import datetime
from Portfolio.styles.styles import Size as Size
from Portfolio.styles.colors import Color as Color
from Portfolio.styles.colors import TextColor as TextColor
import Portfolio.styles.styles as styles

def footer() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.vstack(
                rx.text(
                    "Web desarrollada por Josep Guiu Sillés", 
                    font_size=Size.MEDIUM.value),
                rx.spacer(),
                rx.text(
                    "Versión actual -> V.1", 
                    font_size=Size.MEDIUM.value)
            ),
            rx.spacer(),
            rx.vstack(
                rx.text(
                    "Página personal", 
                    font_size=Size.MEDIUM.value),
                rx.spacer(),
                rx.text(
                    "Repositorio de GITHUB", 
                    font_size=Size.MEDIUM.value)
            ),
        ),
        rx.spacer(),
        rx.hstack(
            rx.image(
                src="fotoperfil.jpg",
                width="auto",
                height= Size.VERY_BIG.value,
                style= styles.border_image_foot,
                alt= "Logotipo de josep, una \"D\" dentro de un circulo"
            ),
        ),
        margin_bottom= Size.BIG.value,
        padding_y= Size.SMALL.value,
        padding_x= Size.BIG.value,
        color= TextColor.FOOTER.value,
        align_items="center",
        width="100%",
        border="solid 1px green"
    )