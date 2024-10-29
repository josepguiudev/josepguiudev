import reflex as rx
import Portfolio.styles.styles as styles

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        style= styles.title_style,
        size= "4"
    )