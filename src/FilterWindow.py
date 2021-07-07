from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QRadioButton

class FilterWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # TODO:
        # Title should be arbitrary text
        # Ingredient should use a radix search for existing ingredients
        # Nutrients and dietary requirements should do the same
        # Prep and cook times should be in days, hours, and minutes
        # Total time is just the sum of the two

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Search filters"))
        for label in ["Title", "Ingredient", "Nutrient", "Dietary", "Prep Time", "Cook Time", "Total Time"]:
            layout.addWidget(self._createSearchOption(label))


        self.setLayout(layout)

    def _createSearchOption(self, label):
        widget = QWidget()

        layout = QHBoxLayout()
        layout.addWidget(QLabel(label))
        layout.addWidget(QLineEdit())

        widget.setLayout(layout)
        return widget
