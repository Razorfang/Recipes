#!/usr/bin/python

from PySide6.QtWidgets import QApplication
import sqlite3
import os

from MainWindow import MainWindow

if __name__ == "__main__":

    # Change to directory this file is stored in
    os.chdir(os.path.dirname(__file__))
    dbFile = "../database/recipes.sqlite3"

    # Create application
    app = QApplication()

    # Connect to recipe database
    con = sqlite3.connect(dbFile)
    cur = con.cursor()

    # Show all ingredients
    text = ""
    for row in cur.execute("SELECT ingredient_description FROM ingredients;"):
        text += f'{row[0]}||||\n'

    con.close()

    # Create the main window
    mainWindow = MainWindow(title=text)
    mainWindow.show()

    # Run application
    app.exec()
