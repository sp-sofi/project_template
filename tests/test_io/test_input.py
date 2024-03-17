import unittest
import pandas as pd
from app.io.input import input_text, read_from_file, read_from_file_pandas

class TestInputFunctions(unittest.TestCase):
    def test_read_from_file(self):
        file_content = read_from_file("../../test_data.txt")
        self.assertEqual(file_content, "This is a test text")

    def test_read_from_file_pandas(self):
        dataframe = read_from_file_pandas("../../data.csv")
        self.assertTrue(dataframe is not None)
        self.assertEqual(dataframe.shape, (2, 1))

if __name__ == '__main__':
    unittest.main()
