import reflex as rx
from Portfolio.components.email_button import email_button
from Portfolio.components.title import title 
from Portfolio.styles.styles import Size, MAX_WIDTH

def links() -> rx.Component:
    return rx.vstack(
        title("CONTACTO"),
        email_button(
            "Email", 
            "Envíame un correo electrónico si quieres contactar conmigo", 
            "Josep.Guiu.Dev@gmail.com", 
            f"mailto:{"josep.guiu.s@gmail.com"}"),
        width= "100%",
        spacing= Size.DEFAULT.value,
        max_width= MAX_WIDTH,
        margin_y= Size.BIG.value
    )