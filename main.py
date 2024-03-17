from app.io.input import input_text, read_from_file, read_from_file_pandas
from app.io.output import output_text, write_to_file


def main():
    # console input output
    text_input = input_text()
    print("You entered: ")
    output_text(text_input)

    #reading from file using bult in functions
    print("\nreading using python functions from data.csv:")
    file_content = read_from_file("data_to_read.csv")
    output_text(file_content)
    print("data written to output_python.py\n")

    #reading using pandas functions
    print("reading using pandas from data.csv: ")
    dataframe = read_from_file_pandas("data.csv")
    output_text(str(dataframe))
    print("\ndata written to output_pandas.py")
    write_to_file(str(dataframe), "data/output_pandas.txt")


if __name__ == "__main__":
    main()
