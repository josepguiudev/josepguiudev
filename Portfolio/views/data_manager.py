import reflex as rx
from Portfolio.styles.styles import body_style_size
from Portfolio.components.title import title 
from Portfolio.components.knowledge_card import knowledge_card
import Portfolio.constants as Constants 

def data_manager() -> rx.Component:
    return rx.box(
        rx.vstack(
            title("GESTORES DE DATOS"),
            rx.grid(
                rx.foreach(Constants.data_manager, knowledge_card),
                columns="3",
                spacing="4",    
                style=body_style_size,
                border="solid 1px red"
            ),
        ),
        style=body_style_size,
        border="solid 1px green"
    )