from app.io.input import input_console, read_file_builtin, read_file_pandas
from app.io.output import print_console, write_file_builtin

def main():
    text = input_console()
    print_console(text)

    file_text = read_file_builtin("data/input.txt")
    print_console(file_text)

    pandas_text = read_file_pandas("data/input.csv")
    print_console(pandas_text)

    write_file_builtin("data/output.txt", text)


if __name__ == "__main__":
    main()