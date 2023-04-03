import csv
from gspread.exceptions import WorksheetNotFound
from gsheetquery import SPREADSHEET_FILENAME_PREFIX


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

    def list_tables(self):
        """
        Return a list of the tables (sheets) in this database (spreadsheet).

        :return: A list of the table names.
        """
        return [w.title for w in self.spreadsheet.worksheets()]

    def add_table(self, name):
        """
        Create a table with @name.

        :param name: The name of the table to be created.
        """
        try:
            self.spreadsheet.worksheet(name)
        except WorksheetNotFound:
            self.spreadsheet.add_worksheet(name, 10, 10)

    def drop_table(self, name):
        """
        Deletes a table with @name.

        :param name: The name of the table to be deleted.
        """
        try:
            worksheet = self.spreadsheet.worksheet(name)
            self.spreadsheet.del_worksheet(worksheet)
        except WorksheetNotFound:
            pass

    def export_table_csv(self, name, csv_path):
        """
        Exports a table to a csv file.

        :param name: The name of the table to be exported.
        :param csv_path: The path where the csv file will be exported.
        """
        try:
            worksheet = self.spreadsheet.worksheet(name)
            rows = worksheet.get_all_values()
            with open(csv_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(rows)
        except WorksheetNotFound:
            print("Worksheet not found")
