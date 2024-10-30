import reflex as rx
from Portfolio.styles.styles import Size
from Portfolio.styles.styles import Color, body_style_size

def experience_item(company_name) -> rx.Component:
    return rx.flex(
            rx.box(
                rx.avatar(
                    src=f"{company_name["image"]}",
                    size="4",
                    alt= "Logotipo de empresa donde se ha tenido experiencia",
                    radius="full",
                    fallback=f"{company_name["initials"]}",
                    border=f"2px solid {Color.COLOR_HOVER.value}"
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