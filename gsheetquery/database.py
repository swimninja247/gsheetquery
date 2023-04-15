from gspread.exceptions import WorksheetNotFound
from gsheetquery import SPREADSHEET_FILENAME_PREFIX
from gsheetquery.collection import Collection

from typing import List


class Database:
    """
    A class representing a database.  This is the equivalent of a sheets file.
    """

    def __init__(self, spreadsheet) -> None:
        """
        Initialize the Database object.

        :param spreadsheet: The spreadsheet object containing the database.
        """
        self.spreadsheet = spreadsheet

    def get_name(self):
        """
        Return the canonical name of this database.

        :return: The name of the database.
        """
        return self.spreadsheet.title[len(SPREADSHEET_FILENAME_PREFIX) :]

    def list_collection_names(self) -> List[str]:
        """
        Return a list of the collections (sheets) in this database (spreadsheet).

        :return: A list of the table names.
        """
        return [w.title for w in self.spreadsheet.worksheets()]

    def get_collection(self, name: str) -> Collection:
        """
        Get a collection with @name.  If the collection does not exist, create it.

        :param name: The name of the collection to get.
        """
        return self.create_collection(name)

    def create_collection(self, name: str) -> Collection:
        """
        Create a collection with @name.  If the collection already exists, return the existing collection.

        :param name: The name of the collection to be created.
        """
        try:
            return Collection(self.spreadsheet.worksheet(name))
        except WorksheetNotFound:
            return Collection(self.spreadsheet.add_worksheet(name, 10, 10))

    def drop_collection(self, name: str) -> None:
        """
        Deletes a table with @name.

        :param name: The name of the table to be deleted.
        """
        try:
            worksheet = self.spreadsheet.worksheet(name)
            self.spreadsheet.del_worksheet(worksheet)
        except WorksheetNotFound:
            pass

    # TODO: don't create duplicate collection objects
    def __getitem__(self, name: str) -> Collection:
        """
        Get a collection (sheet) by name from this database (spreadsheet).

        :param name: The name of the collection to be retrieved.
        :return: A collection object.
        """
        return self.get_collection(name)
