def output_to_console(data):
    """
    Prints data to console

    Args:
        data (str): Data to print
    Returns:
        None: Result prints to console
    """
    print(data)


def write_file_python(data):
    """
    Writes data to file.txt in data folder using python built-in capabilities

    Args:
        data (str): Data to write to the file
    Returns:
        None: Result prints to file
    """
    with open("data/data.txt", "w") as f:
        f.write(data)
