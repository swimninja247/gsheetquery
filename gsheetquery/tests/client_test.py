from unittest.mock import patch, MagicMock
import unittest
import gspread
from gsheetquery.Client import Client
from gsheetquery.Database import Database
from gsheetquery import SPREADSHEET_FILENAME_PREFIX


class TestClient(unittest.TestCase):
    @patch.object(gspread, 'oauth')
    def setUp(self, mock_oauth):
        self.client = Client()
        self.mock_gs = MagicMock()
        self.client._gs = self.mock_gs

    def test_get_database_returns_database_object(self):
        # Arrange
        spreadsheet = MagicMock()
        self.mock_gs.open.return_value = spreadsheet

        # Act
        result = self.client.get_database('test_database')

        # Assert
        self.assertIsInstance(result, Database)
        self.assertEqual(result.spreadsheet, spreadsheet)

    def test_get_database_returns_none_when_spreadsheet_not_found(self):
        # Arrange
        name = 'nonexistent_database'
        self.mock_gs.open = MagicMock(side_effect=gspread.SpreadsheetNotFound)

        # Act
        result = self.client.get_database(name)

        # Assert
        self.assertIsNone(result)

    def test_create_database_returns_existing_database_when_spreadsheet_already_exists(self):
        # Arrange
        name = 'existing_database'
        existing_spreadsheet = MagicMock()
        self.mock_gs.open.return_value = existing_spreadsheet

        # Act
        result = self.client.create_database(name)

        # Assert
        self.assertIsInstance(result, Database)
        self.assertEqual(result.spreadsheet, existing_spreadsheet)
        self.mock_gs.open.assert_called_once_with(SPREADSHEET_FILENAME_PREFIX + name)
        self.mock_gs.create.assert_not_called()

    def test_create_database_creates_new_database_when_spreadsheet_does_not_exist(self):
        # Arrange
        name = 'new_database'
        self.mock_gs.list_spreadsheet_files.return_value = []
        self.mock_gs.open.side_effect = gspread.SpreadsheetNotFound

        # Act
        result = self.client.create_database(name)

        # Assert
        self.assertIsInstance(result, Database)
        self.mock_gs.open.assert_called_once_with(SPREADSHEET_FILENAME_PREFIX + name)
        self.mock_gs.create.assert_called_once_with(title=SPREADSHEET_FILENAME_PREFIX + name)

    def test_list_databases_returns_list_of_database_names(self):
        # Arrange
        titles = ['not_a_database', SPREADSHEET_FILENAME_PREFIX + 'database1']
        mock_files = [{'name': title} for title in titles]
        self.mock_gs.list_spreadsheet_files.return_value = mock_files

        # Act
        result = self.client.list_databases()

        # Assert
        self.assertListEqual(result, [SPREADSHEET_FILENAME_PREFIX + 'database1'])
        self.mock_gs.list_spreadsheet_files.assert_called_once_with()
