from modules.cowsay.greeting import say_message

import gradio as gr
import pandas as pd
import json
from features.cowsay.tab import cowsay_tab
from features.square.tab import square_tab
import dotenv

from pathlib import Path

dotenv.load_dotenv()


with gr.Blocks() as demo:

    # add tabs
    cowsay_tab(gr)
    square_tab(gr)


demo.launch(share=True)
