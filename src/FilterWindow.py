from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QRadioButton

class FilterWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._layout = QHBoxLayout()

        self._label = QLabel("Test")
        self._layout.addWidget(self._label)

        self._button1 = QRadioButton("Button 1")
        self._button1.setChecked(True)
        self._layout.addWidget(self._button1)

        self.setLayout(self._layout)

