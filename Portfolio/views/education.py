import reflex as rx
from Portfolio.components.title import title
from Portfolio.styles.styles import body_style_size

def education() -> rx.Component:
    return rx.vstack(
        title("ESTUDIOS"),
        rx.text(
            "·Estudié desarrollo de aplicaciones multiplataforma",
            rx.text.strong(" (DAM) "),
            "en el \"Centre d'estudis politècnics\"",
            rx.text.strong(" (CEP) "),
            width="100%"
        ),
        title("OTROS"),
        rx.text(
            "· Estudié marketing y relaciones públicas",
            rx.text.strong(" (MARP) "),
            "en el \"Centre d'estudis politècnics\"",
            rx.text.strong(" (CEP) "),
            width="100%"
        ),
        rx.text(
            "· Estudié Bachirato en la",
            rx.text.strong(" \"Escuela Trinitarias\" "),
            width="100%"
        ),
        rx.text(
            "· Realicé las pruebas de acceso a la universidad en",
            rx.text.strong(" \"UAB\" "),
            width="100%"
        ),
        style=body_style_size
    )

