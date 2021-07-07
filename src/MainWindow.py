from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout 
from MenuBar import MenuBar 
from FilterWindow import FilterWindow
from SearchButton import SearchButton

'''
The main window for the application
'''
class MainWindow(QMainWindow):

    def __init__(self, parent=None, title="Recipe Database Application"):
        # Set general properties
        super().__init__(parent)
        self.setWindowTitle(title)

        # Create menu bar
        self.setMenuBar(MenuBar())

        # Create vertical layout containing filters and search button
        filterWidget = QWidget()

        filterLayout = QVBoxLayout()
        filterLayout.addWidget(FilterWindow())
        filterLayout.addWidget(SearchButton())

        filterWidget.setLayout(filterLayout)
        self.setCentralWidget(filterWidget)
