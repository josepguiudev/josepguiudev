import reflex as rx
from Portfolio.styles.styles import Size, body_style_size

def experience_item(avatar_image: str, company_name: str, date: str) -> rx.Component:
    return rx.flex(
            rx.box(
                rx.avatar(
                    src=avatar_image,
                    size="4",
                    alt= "Logotipo de empresa donde se ha tenido experiencia",
                    radius="full",
                    fallback=company_name,
                ),
                margin_right=Size.DEFAULT.value
            ),
            rx.spacer(),
            rx.box(
                rx.text(company_name)
            ),
            rx.spacer(),
            rx.box(
                rx.text(date)
            ),
            align_items="center",
            style= body_style_size,
            margin_y=Size.SUPER_SMALL.value
        )