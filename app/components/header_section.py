import reflex as rx
from app.states.chat_state import ChatState


def header_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.select(
                rx.el.option("Agent", value="Agent"),
                rx.el.option("Team", value="Team"),
                value=ChatState.selected_mode,
                on_change=ChatState.set_selected_mode,
                class_name="bg-[#40414F] text-neutral-300 text-sm rounded-md p-1 border border-neutral-600 focus:outline-none",
            ),
            rx.el.select(
                rx.foreach(
                    ChatState.model_options,
                    lambda option: rx.el.option(option, value=option),
                ),
                value=ChatState.selected_model,
                on_change=ChatState.set_selected_model,
                class_name="bg-[#40414F] text-neutral-300 text-sm rounded-md p-1 border border-neutral-600 focus:outline-none",
            ),
            class_name="flex items-center space-x-2",
        ),
        class_name="bg-[#2A2B2E] px-4 py-2 rounded-lg shadow",
    )