import csv
from gspread.exceptions import WorksheetNotFound
from gsheetquery import SPREADSHEET_FILENAME_PREFIX

"""
A spreadsheet file will represent a database
A sheet will represent a table
Each row is an entry, and each column is an attribute
"""


class Database:
    def __init__(self, spreadsheet) -> None:
        self.spreadsheet = spreadsheet

    """
    Return the canonical name of this database
    """

    def get_name(self):
        return self.spreadsheet.title[len(SPREADSHEET_FILENAME_PREFIX) :]

    """
    Return a list of the tables (sheets) in this database (spreadsheet)
    """

    def list_tables(self):
        return [w.title for w in self.spreadsheet.worksheets()]

    """
    Create a table with @name
    """

    def add_table(self, name):
        try:
            self.spreadsheet.worksheet(name)
        except WorksheetNotFound:
            self.spreadsheet.add_worksheet(name, 10, 10)

    """
    Deletes a table with @name
    """

    def drop_table(self, name):
        try:
            worksheet = self.spreadsheet.worksheet(name)
            self.spreadsheet.del_worksheet(worksheet)
        except WorksheetNotFound:
            pass

    """
    Exports a table to a csv file
    """

    def export_table_csv(self, name, csv_path):
        try:
            worksheet = self.spreadsheet.worksheet(name)
            rows = worksheet.get_all_values()
            with open(csv_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(rows)
        except WorksheetNotFound:
            print("Worksheet not found")
