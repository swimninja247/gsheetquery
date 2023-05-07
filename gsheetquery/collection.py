from gspread import Worksheet
from typing import Dict, List, Optional
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

    def find_one(self, template: Dict[str, str] = None) -> Optional[Dict[str, str]]:
        """
        Returns the first document matching the given template.
        The template is a subset of the values of the document.  Returns None if no matches found.

        :param template: A list of mappings to strings
        """
        search_values = utils.doc_to_row(template)
        print(search_values)

        for i, row in enumerate(self.worksheet.get_values()):
            print(row)
            if all(val in row for val in search_values):
                return utils.row_to_doc(row)

        return None

    def find_many(self, template: Dict[str, str] = None, max: int = 0) -> List[Dict[str, str]]:
        """
        Returns up to max matching documents as in find_one.

        :param template: A list of mappings to strings
        :param max: The max number of results to return.  If 0, returns all.
        """
        search_values = utils.doc_to_row(template)
        result = []

        for i, row in enumerate(self.worksheet.get_values()):
            if all(val in row for val in search_values):
                result.append(utils.row_to_doc(row))
                if len(result) == max:
                    break

        return result
