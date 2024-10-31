import reflex as rx
from Portfolio.components.title import title
from Portfolio.styles.styles import body_style_size

def more_data() -> rx.Component:
    return rx.vstack(
        title("MAS DATOS"),
        rx.text(
            "·Me gusta trabajar usando ",
            rx.text.strong(" \"testing\" "),
            "en micódigo.",
            width="100%"
        ),
        rx.text(
            "·Suelo trabajar mediante el flujo de trabajo de ",
            rx.text.strong(" \"gitflow\" "),
            ". Trabajar sin ello puede hacer el trabajo más difícil.",
            width="100%"
        ),
        style=body_style_size
    )