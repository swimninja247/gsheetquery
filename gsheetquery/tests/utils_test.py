import unittest
from gsheetquery.utils import key_val_to_cell, cell_to_key_val, doc_to_row, row_to_doc


class TestUtils(unittest.TestCase):
    def test_key_val_to_cell(self):
        # Test with valid input
        self.assertEqual(key_val_to_cell("key", "value"), '"key": "value"')

    def test_cell_to_key_val(self):
        # Test with valid input
        self.assertEqual(cell_to_key_val('"key": "value"'), ('key', 'value'))

        # Test with invalid input
        with self.assertRaises(ValueError):
            cell_to_key_val('"key": value')

    def test_doc_to_row(self):
        # Test with valid input
        doc = {"key1": "value1", "key2": "value2"}
        expected_row = ['"key1": "value1"', '"key2": "value2"']
        self.assertEqual(doc_to_row(doc), expected_row)

        # Test with empty input
        doc = {}
        expected_row = []
        self.assertEqual(doc_to_row(doc), expected_row)

    def test_row_to_doc(self):
        # Test with valid input
        row = ['"key1": "value1"', '"key2": "value2"']
        expected_doc = {"key1": "value1", "key2": "value2"}
        self.assertEqual(row_to_doc(row), expected_doc)

        # Test with empty input
        row = []
        expected_doc = {}
        self.assertEqual(row_to_doc(row), expected_doc)
