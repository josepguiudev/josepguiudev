import reflex as rx
from Portfolio.styles.styles import Size, body_style_size
from Portfolio.components.title import title 
import Portfolio.constants as Constants 
from Portfolio.components.knowledge_card import knowledge_card

def languages() -> rx.Component:
    return rx.box(
        rx.vstack(
            title("LENGUAJES"),
            rx.grid(
                rx.foreach(Constants.languages, knowledge_card),
                columns="3",
                spacing="4",    
                style=body_style_size
            ),
        ),
        style=body_style_size
    )