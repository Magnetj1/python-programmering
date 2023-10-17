import os
import sqlite3
from sqlite3 import DataError

def main():
    add_Cats_to_table()


def add_Cats_to_table():
    os.system('clss'if os.name == 'nt'else 'clear')

    hundnamn = input("Mata in hundnamn:")
    hundras = input("Mata in hundras:")
    sqliteConnection = sqlite3.connect("Cats.db")
    cursor = sqliteConnection.cursor()

    sqlite_insert_query = f"""INSERT INTO Cats (namn, ras)VALUES('{hundnamn}''{hundras}')"""
    cursor.execute(sqlite_insert_query)
    cursor.close()
    sqliteConnection.close()



main()