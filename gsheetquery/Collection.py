class Collection:
    """
    A class representing a collection.  This is the equivalent of a single sheet.
    """

    def __init__(self, worksheet) -> None:
        """
        Initialize the Collection object.

        :param spreadsheet: The spreadsheet object containing the database.
        """
        self.worksheet = worksheet
