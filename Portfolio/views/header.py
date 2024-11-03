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
                src="pepeperfil.jpg",
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
                    link_icon("instagram", "https://www.instagram.com/josep.guiu?igsh=MXJ0cnBnYjFldXlsdA=="), #https://reflex.dev/docs/library/data-display/icon/
                    link_icon("linkedin", "https://es.linkedin.com/in/josep-guiu-silles-181290231/de?trk=people-guest_people_search-card"),
                    link_icon("facebook", "https://es-la.facebook.com/josep.guiusilles/"),
                    link_icon("github", "https://github.com/josepguiudev")
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
            """Hola mundo! Este es mi portfolio personal, donde podrás encontrar 
            un poco más de información sobre lo que he ido aprendiendo del sector. 
            Para ver mis proyectos puedes acceder a mi perfil de Github, donde 
            podrás ver el modo en el que trabajo. Si quieres contactar conmigo lo 
            podrás hacer mediante la sección de contacto que encontrarás un poco más abajo.""",
            width="100%"
        ),
        rx.text(
            "Por último, me gustaría recalcar que esta web está hecha con Python.",
            width="100%"
        ),
        style= body_style_size
    )