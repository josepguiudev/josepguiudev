import reflex as rx
import Portfolio.styles.styles as styles
from Portfolio.styles.styles import Size as Size
from Portfolio.styles.colors import Color as Color

def email_button(title: str, body: str, email: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
           rx.hstack(
                rx.icon(
                   tag="arrow-right",
                   width= styles.Size.BIG.value,
                   heigth= styles.Size.DEFAULT.value,
                   margin= Size.DEFAULT.value
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            title,
                            style= styles.button_title_style,
                            color= Color.SECONDARY.value
                        ),
                        rx.text(
                            email,
                            style= styles.button_title_style,
                            color= Color.ACCENT.value
                        ),
                    ),
                    rx.text(
                        body,
                        style= styles.button_body_style,
                        text_align="start"
                    ),
                    spacing= Size.NEW_SMALL.value
                ),
                width= "100%",
                padding_y= Size.SMALL.value,
                padding_right= Size.SMALL.value,
                align_items="center"
           ),
           width= "100%",
           height="auto"
        ),
        href= url,
        is_external= True,
        width= "100%"
    ) 
 