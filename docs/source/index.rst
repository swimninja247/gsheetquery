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

    from gsheetquery import Client, Collection

    # Initialize the client object
    client = Client()

    # Create a new database
    database = client.create_database("my_new_database")

    # Add a new collection to the database
    new_collection = database['new-collection']

    # List the collections in the database
    collection_names = database.list_collection_names()
    print("Collections in the database:", collection_names)

    # Add a doc to the collection
    new_doc = {"name": "Bob", "age", "30"}
    new_collection.insert_one(new_doc)

    # Query the collection
    new_collection.find_one({"age": "30"})

    # Delete the database
    client.drop_collection('new-collection')

API Docs
========

.. toctree::
    :maxdepth: 1

    modules/database
    modules/client
    modules/collection
