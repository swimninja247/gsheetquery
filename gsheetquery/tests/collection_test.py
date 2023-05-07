import unittest
from unittest.mock import MagicMock, patch
from gspread import Worksheet
from gsheetquery.collection import Collection


class CollectionTests(unittest.TestCase):
    def setUp(self):
        # Create a mock Worksheet object for testing
        self.worksheet = MagicMock(spec=Worksheet)
        self.collection = Collection(self.worksheet)
        self.test_doc = {'test': 'test'}
        self.test_docs = [
            ['"name": "Alice"', '"age": "25"', '"gender": "F"'],
            ['"name": "Bob"', '"age": "30"', '"gender": "M"'],
            ['"name": "Charlie"', '"age": "35"', '"gender": "M"'],
        ]
        self.worksheet.get_values.return_value = self.test_docs

    @patch('gsheetquery.utils.doc_to_row')
    def test_insert_one(self, mock_doc_to_row):
        # Assert doc is converted to row and appended
        row_mock = MagicMock()
        mock_doc_to_row.return_value = row_mock

        self.collection.insert_one(self.test_doc)

        mock_doc_to_row.assert_called_once_with(self.test_doc)
        self.worksheet.append_row.assert_called_once_with(row_mock)

    @patch('gsheetquery.utils.doc_to_row')
    def test_insert_many(self, mock_doc_to_row):
        # Test inserting multiple documents into the collection
        row_mock = MagicMock()
        mock_doc_to_row.return_value = row_mock

        self.collection.insert_many([self.test_doc for _ in range(5)])

        self.assertEqual(mock_doc_to_row.call_count, 5)
        self.worksheet.append_rows.assert_called_once_with([row_mock for _ in range(5)])

    def test_find_one_exists(self):
        template = {'age': '30'}
        result = self.collection.find_one(template)

        expected = {'name': 'Bob', 'age': '30', 'gender': 'M'}
        self.assertEqual(result, expected)

    def test_find_one_not_exists(self):
        template = {'name': 'Dave'}
        result = self.collection.find_one(template)
        self.assertIsNone(result)

    def test_find_many_hit_max(self):
        template = {'gender': 'M'}
        result = self.collection.find_many(template, max=1)
        expected = [{'name': 'Bob', 'age': '30', 'gender': 'M'}]
        self.assertEqual(result, expected)

    def test_find_many_found_none(self):
        template = {'name': 'Dave'}
        result = self.collection.find_many(template)

        expected = []
        self.assertEqual(result, expected)

    def test_find_many_found_all(self):
        template = {'gender': 'M'}
        result = self.collection.find_many(template)
        expected = [{'name': 'Bob', 'age': '30', 'gender': 'M'}, {'name': 'Charlie', 'age': '35', 'gender': 'M'}]
        self.assertEqual(result, expected)
