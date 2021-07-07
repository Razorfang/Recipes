from PySide6.QtWidgets import QPushButton

class SearchButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Search recipes")
        self.clicked.connect(self._onClick)

    def _onClick(self):
        print("Click")

