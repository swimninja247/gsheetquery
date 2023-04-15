import gspread
from gspread.exceptions import SpreadsheetNotFound

from gsheetquery import SPREADSHEET_FILENAME_PREFIX
from gsheetquery.database import Database


class Client:
    """
    A class representing a client for accessing Google Sheets API.
    """

    def __init__(self) -> None:
        """
        Initialize the Client object.
        """
        self._gs = gspread.oauth()

    def get_database(self, name):
        """
        Get the spreadsheet file associated with a database.

        :param name: The name of the database to retrieve.
        :return: A Database object representing the spreadsheet file, or None if the file was not found.
        """
        full_name = SPREADSHEET_FILENAME_PREFIX + name
        try:
            spreadsheet = self._gs.open(full_name)
            return Database(spreadsheet)

        except SpreadsheetNotFound:
            print(f"Spreadsheet '{full_name}' not found in your Google Drive account.")
            return None

    def create_database(self, name):
        """
        Create a new spreadsheet file with the given name.

        :param name: The name of the spreadsheet to create.
        :return: A Database object representing the newly created spreadsheet file.
        """
        full_name = SPREADSHEET_FILENAME_PREFIX + name
        try:
            spreadsheet = self._gs.open(full_name)
            return Database(spreadsheet)

        except SpreadsheetNotFound:
            return Database(self._gs.create(title=full_name))

    def del_database(self, name):
        """
        Delete a spreadsheet file associated with a database.

        :param name: The name of the database to delete.
        """
        full_name = SPREADSHEET_FILENAME_PREFIX + name
        try:
            id = self._gs.open(full_name).id
        except SpreadsheetNotFound:
            return

        self._gs.del_spreadsheet(id)

    def list_databases(self):
        """
        Return a list of databases in the user's Google Drive.

        :return: A list of database names.
        """
        files = self._gs.list_spreadsheet_files()
        database_filenames = [file['name'] for file in files if file['name'].startswith(SPREADSHEET_FILENAME_PREFIX)]
        return database_filenames
