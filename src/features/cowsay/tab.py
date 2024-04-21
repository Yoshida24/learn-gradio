from modules.cowsay.greeting import say_message


def cowsay_tab(gr) -> None:
    with gr.Tab("Cowsay"):
        with gr.Row():
            name_input = gr.Textbox(label="Your Name")
            greet_button = gr.Button("Greet")
        greet_output = gr.Textbox(label="Greeting Output", interactive=False)
        greet_button.click(fn=say_message, inputs=name_input, outputs=greet_output)
