import pandas as pd


def input_from_console():
    """
    Takes user input and returns it

    Returns:
        str: User input in string format
    """
    result = input("Please enter your input: ")
    return result


def read_file_python():
    """
    Reads "data.txt" in data folder

    Returns:
        str: Text read from data.txt
    """
    with open("data/data.txt") as f:
        result = f.read()
    return result


def read_file_pandas():
    result = pd.read_csv("data/data.txt", header=None)
    return result
