import unittest
from unittest.mock import MagicMock, patch, mock_open
from gspread import Spreadsheet, Worksheet
from gspread.exceptions import WorksheetNotFound
from gsheetquery.Database import Database
from gsheetquery import SPREADSHEET_FILENAME_PREFIX


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.mock_spreadsheet = MagicMock(spec=Spreadsheet)
        self.database = Database(self.mock_spreadsheet)

    def test_get_name(self):
        self.mock_spreadsheet.title = SPREADSHEET_FILENAME_PREFIX + "test_database"

        # Act and Assert
        self.assertEqual(self.database.get_name(), "test_database")

    def test_list_tables(self):
        mock_worksheets = [MagicMock(spec=Worksheet, title='1'), MagicMock(spec=Worksheet, title='2')]
        self.mock_spreadsheet.worksheets.return_value = mock_worksheets

        # Act and assert
        self.assertEqual(self.database.list_tables(), ['1', '2'])

    def test_add_table_exists(self):
        existing_table = 'existing_table'
        self.database.add_table(existing_table)
        self.mock_spreadsheet.worksheet.assert_called_once_with(existing_table)

    def test_add_table_new(self):
        mock_worksheet = MagicMock(spec=Worksheet)
        self.mock_spreadsheet.worksheet.side_effect = WorksheetNotFound
        self.mock_spreadsheet.add_worksheet.return_value = mock_worksheet

        # Act and assert
        self.assertEqual(self.database.add_table("new_table"), None)
        self.mock_spreadsheet.add_worksheet.assert_called_once_with("new_table", 10, 10)

    def test_drop_table_exists(self):
        mock_worksheet = MagicMock(spec=Worksheet)
        self.mock_spreadsheet.worksheet.return_value = mock_worksheet

        # Act and assert
        self.assertEqual(self.database.drop_table("existing_table"), None)
        self.mock_spreadsheet.del_worksheet.assert_called_once_with(mock_worksheet)

    def test_drop_table_not_exists(self):
        self.mock_spreadsheet.worksheet.side_effect = WorksheetNotFound
        self.database.drop_table('none')
        self.mock_spreadsheet.del_worksheet.assert_not_called()

    @patch('builtins.print')
    def test_export_table_csv_not_found(self, mock_print):
        mock_worksheet = MagicMock(spec=Worksheet)
        self.mock_spreadsheet.worksheet.side_effect = WorksheetNotFound
        self.mock_spreadsheet.worksheet.return_value = mock_worksheet

        self.database.export_table_csv('test', 'test.csv')

        mock_worksheet.get_all_values.assert_not_called()
        mock_print.assert_called_once_with('Worksheet not found')

    @patch('builtins.open', new_callable=mock_open)
    def test_export_table_csv(self, mock_file):
        mock_worksheet = MagicMock(spec=Worksheet)
        self.mock_spreadsheet.worksheet.return_value = mock_worksheet
        csv_path = "test.csv"
        expected_rows = [["1", "2", "3"], ["4", "5", "6"]]
        mock_worksheet.get_all_values.return_value = expected_rows

        self.database.export_table_csv("existing_table", csv_path)

        mock_worksheet.get_all_values.assert_called_once()
        mock_file.assert_called_once_with(csv_path, "w", newline="")
