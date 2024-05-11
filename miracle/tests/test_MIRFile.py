import unittest
import os
from miracle.MIRFile import MIRFile


class TestMIRFile(unittest.TestCase):

    def setUp(self):
        # This method will be run before each test
        self.valid_path = "test_file.MIR"
        self.invalid_path = "test_file.txt"
        self.empty_file_path = "empty_file.MIR"

        # Create a test .MIR file with some content
        with open(self.valid_path, "wb") as f:
            f.write(b"This is a test .MIR file content")

        # Create an empty .MIR file
        with open(self.empty_file_path, "wb") as f:
            pass

    def tearDown(self):
        # This method will be run after each test
        # Clean up the test files
        if os.path.exists(self.valid_path):
            os.remove(self.valid_path)
        if os.path.exists(self.empty_file_path):
            os.remove(self.empty_file_path)

    def test_initialization(self):
        mir_file = MIRFile()
        self.assertEqual(mir_file.path, "")
        self.assertEqual(mir_file.header, {})
        self.assertEqual(mir_file.body, {})

    def test_set_file_path(self):
        mir_file = MIRFile()
        mir_file.set_file_path(self.valid_path)
        self.assertEqual(mir_file.path, self.valid_path)

    def test_read_bytes_valid_file(self):
        mir_file = MIRFile(self.valid_path)
        data = mir_file.read_bytes()
        self.assertIsInstance(data, bytes)

    def test_read_bytes_invalid_extension(self):
        mir_file = MIRFile(self.invalid_path)
        with self.assertRaises(Exception) as context:
            mir_file.read_bytes()
        self.assertTrue(
            "The specified file is not of .MIR format" in str(context.exception)
        )

    def test_read_bytes_empty_file(self):
        mir_file = MIRFile(self.empty_file_path)
        with self.assertRaises(Exception) as context:
            mir_file.read_bytes()
        self.assertTrue(
            "The specified .MIR file was empty and cannot be parsed"
            in str(context.exception)
        )


if __name__ == "__main__":
    unittest.main()
