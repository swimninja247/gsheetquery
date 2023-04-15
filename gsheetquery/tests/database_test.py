import unittest
from unittest.mock import MagicMock
from gspread import Spreadsheet, Worksheet
from gspread.exceptions import WorksheetNotFound
from gsheetquery.database import Database
from gsheetquery.collection import Collection
from gsheetquery import SPREADSHEET_FILENAME_PREFIX


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.mock_spreadsheet = MagicMock(spec=Spreadsheet)
        self.database = Database(self.mock_spreadsheet)

    def test_get_name(self):
        self.database.spreadsheet.title = SPREADSHEET_FILENAME_PREFIX + "test_database"

        # Act and Assert
        self.assertEqual(self.database.get_name(), "test_database")

    def test_list_collection_names(self):
        mock_worksheets = [MagicMock(spec=Worksheet, title='1'), MagicMock(spec=Worksheet, title='2')]
        self.database.spreadsheet.worksheets.return_value = mock_worksheets

        # Act and assert
        self.assertEqual(self.database.list_collection_names(), ['1', '2'])

    def test_create_collection_exists(self):
        name = "existing_collection"
        worksheet_mock = MagicMock(spec=Worksheet)
        self.database.spreadsheet.worksheet.return_value = worksheet_mock

        result = self.database.create_collection(name)

        self.database.spreadsheet.worksheet.assert_called_once_with(name)
        self.database.spreadsheet.add_worksheet.assert_not_called()
        self.assertEqual(result.worksheet, Collection(worksheet_mock).worksheet)

    def test_create_collection_new(self):
        name = "new_collection"
        worksheet_mock = MagicMock(spec=Worksheet)
        self.database.spreadsheet.worksheet.side_effect = WorksheetNotFound("Not found")
        self.database.spreadsheet.add_worksheet.return_value = worksheet_mock

        result = self.database.create_collection(name)

        self.database.spreadsheet.worksheet.assert_called_once_with(name)
        self.database.spreadsheet.add_worksheet.assert_called_once_with(name, 10, 10)
        self.assertEqual(result.worksheet, Collection(worksheet_mock).worksheet)

    def test_drop_collection_exists(self):
        # Test dropping an existing collection
        name = "existing_collection"
        worksheet_mock = MagicMock(spec=Worksheet)
        self.database.spreadsheet.worksheet.return_value = worksheet_mock

        self.database.drop_collection(name)

        self.database.spreadsheet.worksheet.assert_called_once_with(name)
        self.database.spreadsheet.del_worksheet.assert_called_once_with(worksheet_mock)

    def test_drop_collection_not_exists(self):
        # Test dropping a collection that does not exist
        name = "nonexistent_collection"
        self.database.spreadsheet.worksheet.side_effect = WorksheetNotFound("Not found")

        self.database.drop_collection(name)

        self.database.spreadsheet.worksheet.assert_called_once_with(name)
        self.database.spreadsheet.del_worksheet.assert_not_called()

    def test_get_collection(self):
        collection_mock = MagicMock(spec=Collection)
        self.database.create_collection = MagicMock(return_value=collection_mock)

        result = self.database.get_collection('test')

        self.database.create_collection.assert_called_once()
        self.assertEqual(result, collection_mock)

    def test_getitem(self):
        collection_mock = MagicMock(spec=Collection)
        self.database.get_collection = MagicMock(return_value=collection_mock)

        result = self.database['test']

        self.database.get_collection.assert_called_once()
        self.assertEqual(result, collection_mock)
