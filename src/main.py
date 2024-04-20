from modules.cowsay.greeting import say_message

import gradio as gr
import dotenv

dotenv.load_dotenv()


demo = gr.Interface(
    fn=say_message,
    inputs=["text", "slider"],
    outputs=["text"],
    title="Cowsay App",
    description="Enter your message to receive a cow's message!",
)

demo.launch(share=True)
