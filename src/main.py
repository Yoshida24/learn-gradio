import gradio as gr
from features.cowsay.tab import cowsay_tab
from features.csv_transformation.tab import csv_transformation_tab
import dotenv


dotenv.load_dotenv()


with gr.Blocks() as demo:
    # add tabs
    csv_transformation_tab(gr)
    cowsay_tab(gr)


demo.launch(share=False)
