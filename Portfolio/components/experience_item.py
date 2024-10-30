import reflex as rx
from Portfolio.styles.styles import Size, body_style_size
import Portfolio.constants as Constants 

def experience_item(company_name) -> rx.Component:
    return rx.flex(
            rx.box(
                rx.avatar(
                    #src=avatar_image,
                    size="4",
                    alt= "Logotipo de empresa donde se ha tenido experiencia",
                    radius="full",
                    #fallback=Constants.companies[f"{company_name}"],
                ),
                margin_right=Size.DEFAULT.value
            ),
            rx.spacer(),
            rx.box(
                rx.text(company_name["name"])
            ),
            rx.spacer(),
            rx.box(
                rx.text(company_name["date"])
            ),
            align_items="center",
            style= body_style_size,
            margin_y=Size.SUPER_SMALL.value
        )