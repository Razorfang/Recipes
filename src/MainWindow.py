from PySide6.QtWidgets import QMainWindow
from MenuBar import MenuBar 

'''
The main window for the application
'''
class MainWindow(QMainWindow):

    def __init__(self, parent=None, title="Recipe Database Application"):
        super().__init__(parent)
        self.setWindowTitle(title)

        self._menuBar = MenuBar()
        self.setMenuBar(self._menuBar)
