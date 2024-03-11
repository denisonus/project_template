from app.io import input, output


def main():
    data_1 = input.input_from_console()
    output.output_to_console(data_1)
    output.write_file_python(data_1)

    data_2 = input.read_file_python()
    output.output_to_console(data_2)
    output.write_file_python(data_2)

    data_3 = input.read_file_pandas()
    output.output_to_console(data_3)
    output.write_file_python(str(data_3))


if __name__ == '__main__':
    main()
