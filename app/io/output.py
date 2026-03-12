def print_console(text):
    print(text)


def write_file_builtin(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)