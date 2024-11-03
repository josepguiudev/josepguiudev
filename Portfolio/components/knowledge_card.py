import reflex as rx
from Portfolio.styles.styles import Size
from Portfolio.styles.styles import body_style_size

def knowledge_card(language) -> rx.Component:
    return rx.card(
            rx.flex(
                rx.link(
                    rx.avatar(
                        src=language["image"],
                        alt="logo lenguaje de programación",
                        fallback=language["initials"],
                        object_fit="contain"
                    ),
                    rx.box(
                        rx.text(
                            language["name"],
                            text_align="center"
                        )
                    ),
                    href=language["url"],
                    is_external=True
                ),
                spacing="2",
                align_items="center",
                style= body_style_size,
                margin_y=Size.SUPER_SMALL.value,
                direction="column"
            ),
            width="100%"
        )