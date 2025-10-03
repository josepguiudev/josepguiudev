import reflex as rx
from Portfolio.styles.styles import Size, Color

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text("Josep Guiu Sillés"),
            rx.spacer(),
            rx.text("JosepGuiuDev@gmail.com"),
            rx.link(
                "Currículum",
                href="https://drive.google.com/file/d/1emagXMreXEaYleNW-BuigMycjtbWSF0f/view?usp=drive_link",
                download=True,
                target="_blank",
                color="#3399FF",  # Azul claro
                font_weight="bold",
                text_decoration="underline"
            ),
            width="100%"
        ),
        bg=Color.NAVBAR_COLOR.value,
        position="sticky",
        border_bottom=f"0.25em solid {Color.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )