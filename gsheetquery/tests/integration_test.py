from gsheetquery.Client import Client
import pytest


@pytest.mark.skip(reason="need to automate google api auth")
def test_client():
    client = Client()

    # del test database
    client.del_database('test')

    # create database
    db = client.create_database('test')
    assert client.list_databases() == ['GSHEETQUERY_test']
    assert db.get_name() == 'test'

    db = client.get_database('test')
    assert db.get_name() == 'test'

    # test database
    db.add_table('test_table')
    assert db.list_tables() == ['Sheet1', 'test_table']
    db.drop_table('test_table')
