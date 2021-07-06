from PySide6.QtWidgets import QMainWindow, QGroupBox, QVBoxLayout, QHBoxLayout, QGridLayout
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
        #self.setLayout(QVBoxLayout())

        # Create menu bar
        self._menuBar = MenuBar()
        self.setMenuBar(self._menuBar)

        # Window containing search filters
        self._filterWindow = FilterWindow()
        #self._filterWindow.show()

        # Search button
        #self._searchButton = SearchButton()
        #self._searchButton.show()

        # Split these two into a grid layout
        #filterLayout = QVBoxLayout()
        #filterLayout.addWidget(self._filterWindow)


        #self.setLayout(filterLayout)
        self.setCentralWidget(self._filterWindow)
        #self._filterGroup = QGroupBox("Find Recipes")
        #self._filterGroup.setLayout(QVBoxLayout())
        #self.layout().addWidget(self._filterGroup)
        #self.layout().addStretch()

        #self._filters = QHBoxLayout()
        #self._filters.addWidget(self._filterWindow)
        #self._filterGroup.addLayout(self._filters)
