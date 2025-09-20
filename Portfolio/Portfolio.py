import reflex as rx
import Portfolio.styles.styles as styles
from Portfolio.views.navbar import navbar
from Portfolio.views.header import header
from Portfolio.views.education import education
from Portfolio.views.languages import languages
from Portfolio.views.data_manager import data_manager
from Portfolio.views.used_ide import used_ide
from Portfolio.views.contact import contact
from Portfolio.views.experience import experience
from Portfolio.views.more_data import more_data
from Portfolio.views.footer import footer

class State(rx.State):
    pass


def index() -> rx.Component:
    # (Index), aquí se pondrans las views para que se printeen a la web
    # Nueva prueba
    return rx.box(
        navbar(), 
        rx.center(
            rx.vstack(
                header(),
                education(),
                languages(),
                data_manager(),
                used_ide(),
                experience(),
                more_data(),
                contact()
            )
        ),
        footer()
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

app.add_page(
    index,
    title= "Web Personal de Josep Guiu",
    description="Programador junior buscando trabajo",
    image="fotoperfil.jpg"
    )
