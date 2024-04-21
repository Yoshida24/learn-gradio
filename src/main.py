import gradio as gr
import pandas as pd
import json
from features.cowsay.tab import cowsay_tab
from features.square.tab import square_tab
import dotenv

from pathlib import Path

dotenv.load_dotenv()


def preview_csv(file):
    # CSVファイルを読み込む
    df = pd.read_csv(file)
    if len(df) < 6:
        return df
    else:
        # 最初の3行と最後の3行を選択
        preview_df = pd.concat([df.head(3), df.tail(3)])
        return preview_df


def create_csv_file(df, filepath: str = "tmp/download_data.csv") -> str:
    # パスが存在しない場合はディレクトリを作成
    Path(filepath).parent.mkdir(exist_ok=True)
    # データフレームをCSV形式で保存
    df.to_csv(filepath, index=False)
    # pathを計算し返す
    return filepath


def add_json_profile(df):
    # DataFrameの各行にJSONプロフィールを追加
    result = []
    for _, row in df.iterrows():
        profile = json.dumps(dict(row))
        result.append(profile)
    df["JSON Profile"] = result
    # プレビュー用に最初の3行と最後の3行を返す
    preview_df = pd.concat([df.head(3), df.tail(3)])
    filepath = create_csv_file(df)
    return (df, preview_df, filepath)


def download_data(df):
    # データフレームをCSV形式でダウンロードするための関数
    return df.to_csv()


with gr.Blocks() as demo:

    with gr.Tab("CSV Transformation"):
        gr.Markdown("### CSVファイルアップロードとJSONプロフィール追加デモ")

        with gr.Row():
            file_input = gr.File(label="CSVファイルをアップロードしてください")
        output_table = gr.Dataframe()
        file_input.change(preview_csv, inputs=file_input, outputs=output_table)

        # JSONプロフィールを追加するボタンと処理
        add_json_button = gr.Button("JSONプロフィールを追加")
        output_table_with_json = gr.Dataframe()
        output_full_json = gr.Dataframe(
            visible=False
        )  # 完全なデータを保持するための非表示のデータフレーム
        output_json_file = gr.File(label="Download JSON Profile")
        add_json_button.click(
            fn=add_json_profile,
            inputs=output_table,
            outputs=[output_full_json, output_table_with_json, output_json_file],
        )

    # add tabs
    cowsay_tab(gr)
    square_tab(gr)


demo.launch(share=True)
