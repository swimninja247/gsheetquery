# GSheetQuery
GSheetQuery is a python library for using Google Sheets as a database.  It provides an ORM and query builder.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Open Issues](https://img.shields.io/github/issues/swimninja247/gsheetquery)
[![Build Status](https://github.com/swimninja247/gsheetquery/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/swimninja247/gsheetquery/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/swimninja247/gsheetquery/branch/main/graph/badge.svg)](https://codecov.io/gh/swimninja247/gsheetquery)
[![PyPI](https://img.shields.io/pypi/v/gsheetquery)](https://pypi.org/project/gsheetquery/)

## Overview

For small projects, full Python frameworks can be overkill (Django), especially if you want code up and running quickly.  Google Sheets can be leveraged as a database and made accessible by GSheetQuery.

This library will allow users to interact with google sheets as a document database similar to MongoDB.

## Install

Install using `pip install gsheetquery` in your preferred command line.  Import to your python files like any other module.

## Quickstart

```python
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
```