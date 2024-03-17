def output_text(text):
    """
    Function to output text to the console.

    Args:
        text (str): The text to be displayed.
    """
    print(text)

def write_to_file(data, file_path):
    """
    Function to write data to a file using built-in Python capabilities.

    Args:
        data: The data to be written to the file.
        file_path (str): The path to the file where data will be written.
    """
    with open(file_path, 'w') as file:
        file.write(data)
