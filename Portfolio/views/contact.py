import reflex as rx
from Portfolio.components.email_button import email_button
from Portfolio.components.title import title 
from Portfolio.styles.styles import Size, body_style_size

def contact() -> rx.Component:
    return rx.vstack(
        title("CONTACTO"),
        email_button(
            "Email", 
            "Envíame un correo electrónico si quieres contactar conmigo", 
            "Josep.Guiu.Dev@gmail.com", 
            f"mailto:{"josepguiudev@gmail.com"}"),
        style=body_style_size
    )