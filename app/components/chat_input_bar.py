import reflex as rx
from app.states.chat_state import ChatState


def chat_input_bar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.foreach(
                ChatState.uploaded_files,
                lambda f: rx.el.div(
                    f,
                    rx.el.button(
                        rx.icon("x", size=12),
                        on_click=ChatState.clear_uploads,
                        class_name="ml-2 text-neutral-400 hover:text-white",
                        size="1",
                    ),
                    class_name="flex items-center text-xs bg-neutral-700 text-neutral-200 px-2 py-1 rounded-md",
                ),
            ),
            class_name="flex flex-wrap gap-2 pb-2 justify-center",
        ),
        rx.el.form(
            rx.el.div(
                rx.el.div(
                    rx.upload.root(
                        rx.el.button(
                            rx.icon(
                                "paperclip", size=18, class_name="text-neutral-400"
                            ),
                            type="button",
                            class_name="p-2 bg-[#40414F] hover:bg-[#50515f] rounded-md",
                        ),
                        on_drop=ChatState.handle_upload(rx.upload_files()),
                        multiple=True,
                    ),
                    rx.el.select(
                        rx.foreach(
                            ChatState.project_options,
                            lambda option: rx.el.option(option, value=option),
                        ),
                        value=ChatState.selected_project,
                        on_change=ChatState.set_selected_project,
                        class_name="bg-[#40414F] text-neutral-300 text-sm rounded-md p-1 border border-neutral-600 focus:outline-none",
                    ),
                    class_name="flex items-center space-x-2 p-2",
                ),
                rx.el.textarea(
                    name="chat_page_prompt_input",
                    placeholder="Reply to Claude...",
                    class_name="flex-grow bg-transparent text-neutral-200 placeholder-neutral-500 focus:outline-none resize-none p-3 leading-tight text-base",
                    rows=1,
                    auto_height=True,
                    max_height="20vh",
                    enter_key_submit=True,
                ),
                rx.el.div(
                    rx.el.button(
                        rx.icon("arrow-up", size=20, class_name="text-white"),
                        type="submit",
                        class_name="p-2.5 bg-[#E97055] hover:bg-[#d3654c] rounded-md aspect-square",
                        is_disabled=ChatState.is_streaming,
                    ),
                    class_name="flex items-center p-2",
                ),
                class_name="bg-[#2A2B2E] rounded-xl shadow-lg w-full flex items-end",
            ),
            on_submit=ChatState.send_chat_page_message,
            reset_on_submit=True,
            class_name="w-full max-w-3xl",
        ),
        class_name="sticky bottom-0 w-full flex flex-col items-center p-4 bg-[#202123] border-t border-neutral-700",
    )