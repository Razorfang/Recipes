#!/usr/bin/python

from PySide6.QtWidgets import QApplication, QLabel
import sqlite3

from MainWindow import MainWindow

if __name__ == "__main__":
    # Create application
    app = QApplication()

    # Connect to recipe database
    con = sqlite3.connect("database/recipes.sqlite3")
    cur = con.cursor()

    # Show all ingredients
    text = ""
    for row in cur.execute("SELECT ingredient_description FROM ingredients;"):
        text += f'{row[0]}||||\n'

    #label = QLabel(text)

    con.close()

    #label.show()

    # Create the main window
    mainWindow = MainWindow(title=text)
    mainWindow.show()

    # Run application
    app.exec()
