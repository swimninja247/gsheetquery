# GSheetQuery
GSheetQuery is a python library for using Google Sheets as a database.  It provides an ORM and query builder.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![Open Issues](https://img.shields.io/github/issues/swimninja247/gsheetquery)

## Overview

For small projects, full Python frameworks can be overkill (Django), especially if you want code up and running quickly.  Google Sheets can be leveraged as a production database and made accessible by GSheetQuery.

This library will allow users to create models via an ORM that will be stored in Google Sheets via the Google API.  This library comes with a query builder too.

## Roadmap

- Create client
    - Connect
    - Build sheets and drive service
    - List databases from metadata spreadsheet
- Represent sheets files as databases
    - There will be a metadata sheet that stores the ids of various databases
- Individual sheets in a file are tables
- Create models interface
