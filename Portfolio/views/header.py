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
                    "Josep Guiu Sillés",
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
                    link_icon("github", "https://github.com/josepguiudev"),
                    link_icon("github", "https://github.com/Josep-Guiu")
                ),
            ),
        spacing=Size.NEW_BIG.value
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
            rx.text("Edad: 31 años"),
            rx.spacer(),
            rx.text("Tlfn: 640648963"),
            rx.spacer(),
            width= "100%",
            padding_x=Size.DEFAULT.value
        ),
        rx.text(
            """He finalizado el ciclo formativo de Desarrollo de Aplicaciones Multiplataforma (DAM) 
            y actualmente curso el ciclo de Desarrollo de Aplicaciones Web (DAW). Durante mi formación, 
            he adquirido una base sólida en el desarrollo de software y me encuentro motivado por aplicar 
            estos conocimientos en un entorno profesional.""",
            width="100%"
        ),
        rx.text(
            """Estoy muy interesado en formar parte de su equipo como estudiante en prácticas, donde pueda 
            contribuir con mi dedicación, compromiso y ganas de aprender, al mismo tiempo que adquiero experiencia 
            práctica valiosa para mi desarrollo profesional.""",
            width="100%"
        ),
        rx.text(
            """Quedo a su disposición para una entrevista, en la que podré ampliar cualquier información que consideren necesaria.""",
            width="100%"
        ),
        rx.text(
            """Agradezco su atención y espero tener la oportunidad de colaborar con ustedes.""",
            width="100%"
        ),
        style= body_style_size
    )