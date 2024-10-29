import reflex as rx
import Portfolio.styles.styles as styles

class State(rx.State):
    pass


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box()

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

app.add_page(
    index,
    title= "Web Personal de Josep Guiu",
    description="Programador junior buscando trabajo",
    image="favicon.ico"
    )
