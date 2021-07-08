from PySide6.QtWidgets import QPushButton

class SearchButton(QPushButton):
    def __init__(self, method, parent=None):
        super().__init__(parent)
        self.setText("Search recipes")
        self.setOnClickMethod(method)

    def setOnClickMethod(self, method):
        self.clicked.connect(method)


