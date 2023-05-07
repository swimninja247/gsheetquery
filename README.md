# GSheetQuery
GSheetQuery is a python library for using Google Sheets as a document database.  It modeled after pymongo's interface.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Open Issues](https://img.shields.io/github/issues/swimninja247/gsheetquery)
[![Build Status](https://github.com/swimninja247/gsheetquery/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/swimninja247/gsheetquery/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/swimninja247/gsheetquery/branch/main/graph/badge.svg)](https://codecov.io/gh/swimninja247/gsheetquery)
[![PyPI](https://img.shields.io/pypi/v/gsheetquery)](https://pypi.org/project/gsheetquery/)
[![ReadTheDocs](https://readthedocs.org/projects/gsheetquery/badge/?version=latest)](https://gsheetquery.readthedocs.io/en/latest/)

## Overview

For small projects, full Python frameworks can be overkill (Django).  Especially if you want code up and running quickly.  Google Sheets can be leveraged as a database and made accessible by GSheetQuery.

This library will allow users to interact with google sheets as a document database similar to MongoDB.

## Install

Install using `pip install gsheetquery` in your preferred command line.  Import to your python files like any other module.

## Quickstart

```python
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
```