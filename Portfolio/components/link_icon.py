import reflex as rx

def link_icon(tag: str, url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag= tag
        ),
        href= url,
        is_external= True
    )