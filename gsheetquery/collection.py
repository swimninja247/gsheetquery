from gspread import Worksheet
from typing import Dict, List
from gsheetquery import utils


class Collection:
    """
    A class representing a collection.  This is the equivalent of a single sheet.
    """

    def __init__(self, worksheet: Worksheet) -> None:
        """
        Initialize the Collection object.

        :param spreadsheet: The spreadsheet object containing the database.
        """
        self.worksheet = worksheet

    def insert_one(self, doc: Dict[str, str]):
        """
        Insert one document into the collection.

        :param doc: A mapping of strings
        """
        row = utils.doc_to_row(doc)
        self.worksheet.append_row(row)

    def insert_many(self, docs: List[Dict[str, str]]):
        """
        Insert multiple document into the collection.

        :param docs: A list of mappings of strings
        """
        rows = [utils.doc_to_row(doc) for doc in docs]
        self.worksheet.append_rows(rows)
