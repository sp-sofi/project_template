import unittest
from app.io.input import read_from_file, read_from_file_pandas


class TestInputFunctions(unittest.TestCase):
    def test_read_from_file(self):
        file_content = read_from_file("../../test_data/test_data.txt")
        self.assertEqual(file_content, "This is a test text")

    def test_read_from_file_empty(self):
        file_content = read_from_file("../../test_data/empty.txt")
        self.assertEqual(file_content, "")
    def test_read_from_file_nonexistent(self):
        file_content = read_from_file("test_data/nonexistent_file.txt")
        self.assertEqual(file_content, 'File not found.')


    def test_read_from_file_pandas(self):
        dataframe = read_from_file_pandas("../../data.csv")
        self.assertTrue(dataframe is not None)

    def test_read_from_file_pandas_size(self):
        dataframe = read_from_file_pandas("../../data.csv")
        self.assertEqual(dataframe.shape, (2, 1))

    def test_read_from_file_pandas_nonexistent_file(self):
        dataframe = read_from_file_pandas("data.csv")
        self.assertEqual(str(dataframe), 'File not found.')


if __name__ == '__main__':
    unittest.main()
