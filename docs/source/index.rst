Welcome to GSheetQuery's documentation!
=======================================

.. contents::
    :depth: 1


Installation
============

To install "gsheetquery" using pip, simply open a terminal and run the following command:

.. code-block:: console

    pip install gsheetquery

This will download and install the latest version of "gsheetquery" and its dependencies. Once the installation is complete, you can import "gsheetquery" into your Python project and start using it.

Note: Make sure you have pip installed on your machine before running the above command.

Quickstart
==========

.. code-block:: Python

    from gsheetquery import Client, Database

    # Initialize the client object
    client = Client()

    # Create a new database
    database = client.create_database("my_new_database")

    # Add a new table to the database
    database.add_table("my_new_table")

    # List the tables in the database
    table_names = database.list_tables()
    print("Tables in the database:", table_names)

    # Export a table to a CSV file
    table_name = "my_new_table"
    csv_path = "my_new_table.csv"
    database.export_table_csv(table_name, csv_path)

    # Delete the database
    client.del_database("my_new_database")

API Docs
========

.. toctree::
    :maxdepth: 1

    modules/database
    modules/client
