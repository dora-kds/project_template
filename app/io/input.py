import pandas as pd
def input_console():
    return input("Enter text: ")


def read_file_builtin(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def read_file_pandas(path):
    df = pd.read_csv(path)
    return df.to_string()