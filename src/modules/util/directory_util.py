from pathlib import Path


def create_csv_file(df, filepath) -> str:
    # パスが存在しない場合はディレクトリを作成
    Path(filepath).parent.mkdir(exist_ok=True)
    # データフレームをCSV形式で保存
    df.to_csv(filepath, index=False)
    # pathを計算し返す
    return filepath
