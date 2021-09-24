
import os

# This is a bad place for this import
import pymysql

def get_db_info():
    """
    This is crappy code.

    :return: A dictionary with connect info for MySQL
    """
    db_host = os.environ.get("DBHOST", None)

    if db_host is None:

        db_info = {
            "host": "projdb6156.czcf5gwsffzy.us-east-1.rds.amazonaws.com",
            "user": "root",
            "password": "12345678",
            "port": 3306,
            "db": "testdb",
            "cursorclass": pymysql.cursors.DictCursor
        }

    else:

        db_info = {
            "host": db_host,
            "user": os.environ.get("DBUSER"),
            "password": os.environ.get("DBPASSWORD"),
            "cursorclass": pymysql.cursors.DictCursor
        }

    return db_info
