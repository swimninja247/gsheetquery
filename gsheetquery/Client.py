import gspread
from gspread.exceptions import SpreadsheetNotFound

from gsheetquery import SPREADSHEET_FILENAME_PREFIX
from gsheetquery.Database import Database

"""
The client represents the main object that users will interact with
"""


class Client:
    def __init__(self) -> None:
        self._gs = gspread.oauth()

    """
    Gets spreadsheet file associated with database.
    """

    def get_database(self, name):
        full_name = SPREADSHEET_FILENAME_PREFIX + name
        try:
            # Try to open the spreadsheet by its name
            spreadsheet = self._gs.open(full_name)
            return Database(spreadsheet)

        except SpreadsheetNotFound:
            # Handle the case where the spreadsheet does not exist
            print(f"Spreadsheet '{full_name}' not found in your Google Drive account.")
            return None

    """
    Creates a spreadsheet file with the given @name.
    """

    def create_database(self, name):
        full_name = SPREADSHEET_FILENAME_PREFIX + name
        # First see if a spreadsheet with this name already exists
        try:
            spreadsheet = self._gs.open(full_name)
            return Database(spreadsheet)

        except SpreadsheetNotFound:
            return Database(self._gs.create(title=full_name))

    def del_database(self, name):
        full_name = SPREADSHEET_FILENAME_PREFIX + name
        try:
            id = self._gs.open(full_name).id
        except SpreadsheetNotFound:
            return

        self._gs.del_spreadsheet(id)

    """
    Returns a list of databases in the user's Drive
    """

    def list_databases(self):
        files = self._gs.list_spreadsheet_files()
        database_filenames = [file['name'] for file in files if file['name'].startswith(SPREADSHEET_FILENAME_PREFIX)]
        return database_filenames
