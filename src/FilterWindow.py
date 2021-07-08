from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit

class FilterWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Layout
        layout = QVBoxLayout()
        # TODO:
        # Prep and cook times should be in days, hours, and minutes
        # Total time is just the sum of the two

        layout.addWidget(QLabel("Search filters"))

        # Create title filter
        self._filterTitle = QLineEdit()
        layout.addWidget(self._createFilter("Title", self._filterTitle))

        # Create ingredient filter
        self._filterIngredient = QLineEdit()
        layout.addWidget(self._createFilter("Ingredient", self._filterIngredient))

        # Create nutrient filter
        self._filterNutrient = QLineEdit()
        layout.addWidget(self._createFilter("Nutrient", self._filterNutrient))

        # Create dietary filter
        self._filterDietary = QLineEdit()
        layout.addWidget(self._createFilter("Dietary", self._filterDietary))

        # Create prep time filter
        self._filterPrepTime = QLineEdit()
        layout.addWidget(self._createFilter("Prep time", self._filterPrepTime))

        # Create cook time filter
        self._filterCookTime = QLineEdit()
        layout.addWidget(self._createFilter("Cook time", self._filterCookTime))

        # Create total time filter
        self._filterTotalTime = QLineEdit()
        layout.addWidget(self._createFilter("Total time", self._filterTotalTime))

        self.setLayout(layout)

    def _createFilter(self, label, widget):
        w = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(QLabel(label))
        layout.addWidget(widget)
        w.setLayout(layout)
        return w

    def getTitleText(self):
        return self._filterTitle.text()

    def getIngredientText(self):
        return self._filterIngredient.text()

    def getNutrientText(self):
        return self._filterNutrient.text()

    def getDietaryText(self):
        return self._filterDietary.text()

    def getPrepTime(self):
        return self._filterPrepTime.text()

    def getCookTime(self):
        return self._filterCookTime.text()

    def getTotalTime(self):
        return self.getPrepTime() + self.getCookTime()
