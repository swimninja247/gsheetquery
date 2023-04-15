import unittest
from unittest.mock import MagicMock, patch
from gspread import Worksheet
from gsheetquery.collection import Collection


class CollectionTests(unittest.TestCase):
    def setUp(self):
        # Create a mock Worksheet object for testing
        self.worksheet = MagicMock(spec=Worksheet)
        self.collection = Collection(self.worksheet)
        self.doc = {'test': 'test'}

    @patch('gsheetquery.utils.doc_to_row')
    def test_insert_one(self, mock_doc_to_row):
        # Assert doc is converted to row and appended
        row_mock = MagicMock()
        mock_doc_to_row.return_value = row_mock

        self.collection.insert_one(self.doc)

        mock_doc_to_row.assert_called_once_with(self.doc)
        self.worksheet.append_row.assert_called_once_with(row_mock)

    @patch('gsheetquery.utils.doc_to_row')
    def test_insert_many(self, mock_doc_to_row):
        # Test inserting multiple documents into the collection
        row_mock = MagicMock()
        mock_doc_to_row.return_value = row_mock

        self.collection.insert_many([self.doc for _ in range(5)])

        self.assertEqual(mock_doc_to_row.call_count, 5)
        self.worksheet.append_rows.assert_called_once_with([row_mock for _ in range(5)])
