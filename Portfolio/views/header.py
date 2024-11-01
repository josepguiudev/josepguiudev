import reflex as rx
import Portfolio.styles.styles as styles
from Portfolio.components.link_icon import link_icon
from Portfolio.styles.styles import Size as Size
from Portfolio.styles.styles import body_style_size
from Portfolio.styles.colors import Color as Color
from Portfolio.styles.colors import TextColor as TextColor

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="fotoperfil.jpg",
                name="Josep Guiu",
                size="7",
                fallback="Pepe",
                radius= "full",
                border= "3px solid",
                border_color= Color.PRIMARY.value,
                alt="Foto perfil de developer"
            ),
            rx.vstack(
                rx.heading(
                    "Josep Guiu",
                    size= "4",
                ),
                rx.text(
                    "@pepeguiu",
                    size= "2",
                    padding_top= "0px !important",
                    margin_top= "-12px !important"
                ),
                rx.hstack(
                    link_icon("instagram", "google.com"), #https://reflex.dev/docs/library/data-display/icon/
                    link_icon("linkedin", "google.com"),
                    link_icon("facebook", "google.com")
                ),
            ),
        spacing= Size.BIG.value
        ),
        rx.flex(
            rx.hstack(
                rx.text(
                    "+2",
                color= Color.SECONDARY.value
                ),
                rx.text(
                    rx.text.strong("años"),
                    " de experiencia.",
                    as_="p"
                ),
            ),
            rx.spacer(),
            rx.text("Edad: 30 años"),
            rx.spacer(),
            rx.text("Tlf: 633740720"),
            rx.spacer(),
            width= "100%",
            padding_x=Size.DEFAULT.value
        ),
        rx.text(
            """Hola a todos, esta web está hecha con Python y con Reflex. De todos modos, la voy a utilizar
            como medio para exponer mis proyectos y también, a modo de comunicación profesional.""",
            width="100%"
        ),
        style= body_style_size
    )