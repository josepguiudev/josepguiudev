import reflex as rx
from Portfolio.styles.styles import body_style_size
from Portfolio.components.title import title 
from Portfolio.components.knowledge_card import knowledge_card
import Portfolio.constants as Constants 

def used_ide() -> rx.Component:
    return rx.box(
        rx.vstack(
            title("ENTORNOS GRAFICOS"),
            rx.grid(
                rx.foreach(Constants.ide_s, knowledge_card),
                columns="3",
                spacing="4",    
                style=body_style_size
            ),
        ),
        style=body_style_size
    )