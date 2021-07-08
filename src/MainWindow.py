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

        self._filterWindow = FilterWindow()
        filterLayout = QVBoxLayout()
        filterLayout.addWidget(self._filterWindow)
        filterLayout.addWidget(SearchButton(method=self.findRecipes))

        filterWidget.setLayout(filterLayout)
        self.setCentralWidget(filterWidget)

    def findRecipes(self):
        print(self._filterWindow.getTitleText())
        print(self._filterWindow.getIngredientText())
        print(self._filterWindow.getNutrientText())
        print(self._filterWindow.getDietaryText())
        print(self._filterWindow.getPrepTime())
        print(self._filterWindow.getCookTime())
        print(self._filterWindow.getTotalTime())
