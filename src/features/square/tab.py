def square(number):
    return number**2


def square_tab(gr) -> None:
    with gr.Tab("Square"):
        with gr.Row():
            number_input = gr.Number(label="Enter a number")
            square_button = gr.Button("Square it!")
        square_output = gr.Number(label="Result", interactive=False)
        square_button.click(fn=square, inputs=number_input, outputs=square_output)
