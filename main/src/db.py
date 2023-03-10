"""
module db_mngt
    makes the querries to access the db through sqlite (serverless)
    the querries are stored as statements in separate sql files
    through a given filename the actual querry is found and executed

===== Imports =====
built_ins
    - sqlite3
    - pathlib

===== Globals =====
db_location
    - path to the db file
querry_location
    - path to the sql files

===== Classes =====
None

===== Functions =====
get_querry_path(str) -> pathlib.Path
    - checks if the sql file exists and returns the path
get_querry_file_content(pathlib.Path) -> str
    - gets the file content
make_querry(str, data)
    - connects to the db and makes the querry

===== Exceptions =====
FileNotFoundError
Exception
"""

import src.config
import sqlite3, pathlib

db_location = src.config.value_get("MAINTENANCE", "db_location")
querry_location = src.config.value_get("MAINTENANCE", "querry_location")

def _get_querry_path(querry_name: str) -> pathlib.Path:
    querry_path = pathlib.Path(querry_location) / f"{querry_name}.sql"
    if not querry_path.exists(): raise FileNotFoundError(f"file {str(querry_path)} was not found")
    return querry_path

def _get_querry_file_content(querry_path: pathlib.Path) -> str:
    with open (querry_path, "r") as open_file:
        return open_file.read()

def make_querry(querry_name: str, data: tuple = None) -> str:

    querry_path = _get_querry_path(querry_name)
    querry = _get_querry_file_content(querry_path)

    result = None

    try:
        db_connection = sqlite3.connect(db_location)
        db_cursor = db_connection.cursor()

        if data:
            result = db_cursor.execute(querry, data).fetchall()
        else:
            result = db_cursor.execute(querry).fetchall()

    except Exception as e:
        #! log(e)
        print(e)
        pass

    finally:
        db_cursor.close()
        db_connection.commit()
        db_connection.close()
        #! log
        return result