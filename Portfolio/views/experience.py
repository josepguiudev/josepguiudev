import reflex as rx
from Portfolio.styles.styles import body_style_size
from Portfolio.components.title import title 
from Portfolio.components.experience_item import experience_item
import Portfolio.constants as Constants 

def experience() -> rx.Component:
    return rx.vstack(
        title("EXPERIENCIA"),
        rx.foreach(Constants.companies, experience_item),
        style=body_style_size,  
        border="1px solid orange"
    )