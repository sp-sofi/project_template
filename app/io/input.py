def input_text():
    """
    Function to input text from the console.

    Returns:
        str: The text entered by the user.
    """
    return input("Enter text: ")

def read_from_file(file_path):
    """
    Function to read from a file using built-in Python capabilities.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content read from the file.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found."

def read_from_file_pandas(file_path):
    """
    Function to read from a file using the pandas library.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        pandas.DataFrame: The data read from the file as a pandas DataFrame.
    """
    try:
        import pandas as pd
        data = pd.read_csv(file_path)  # Assuming the file is a CSV, change as needed
        return data
    except FileNotFoundError:
        return "File not found."
