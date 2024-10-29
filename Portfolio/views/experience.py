import reflex as rx
from Portfolio.styles.styles import body_style_size
from Portfolio.components.title import title 
from Portfolio.components.experience_item import experience_item

def experience() -> rx.Component:
    return rx.vstack(
        title("EXPERIENCIA"),
        experience_item("fotoperfil.jpg", "Nombre de la empresa", "FECHA"),
        experience_item("fotoperfil.jpg", "Nombre de la empresa", "FECHA"),
        experience_item("fotoperfil.jpg", "Nombre de la empresa", "FECHA"),
        experience_item("fotoperfil.jpg", "Nombre de la empresa", "FECHA"),
        style=body_style_size,
        border="1px solid orange"
    )