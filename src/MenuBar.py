from PySide6.QtWidgets import QMenuBar
from sys import exit as sysexit

'''
The menu bar for the application
'''
class MenuBar(QMenuBar):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._createFileOption()
        self._createRecipesOption()
        self._createIngredientOption()
        self._createNutrientOption()
        self._createViewOption()
        self._createHelpOption()

    def _createFileOption(self):
        fileMenu = self.addMenu("&File")
        fileMenu.addAction("Download all recipes", self._downloadAllRecipesAction)
        fileMenu.addAction("Exit", self._exitAction)

    def _downloadAllRecipesAction(self):
        print("X")

    def _exitAction(self):
        sysexit()

    def _createRecipesOption(self):
        recipeMenu = self.addMenu("&Recipes")
        recipeMenu.addAction("Add recipe", self._addRecipeAction)
        recipeMenu.addAction("Delete recipe", self._deleteRecipeAction)

    def _addRecipeAction(self):
        print("Hello")

    def _deleteRecipeAction(self):
        print("Goodbye")

    def _createIngredientOption(self):
        ingredientMenu = self.addMenu("&Ingredients")
        ingredientMenu.addAction("Add ingredient", self._addIngredientAction)
        ingredientMenu.addAction("Delete ingredient", self._deleteIngredientAction)

    def _addIngredientAction(self):
        print("A")

    def _deleteIngredientAction(self):
        print("B")

    def _createNutrientOption(self):
        nutrientMenu = self.addMenu("&Nutrients")
        nutrientMenu.addAction("Add nutrient", self._addNutrientAction)
        nutrientMenu.addAction("Delete nutrient", self._deleteNutrientAction)

    def _addNutrientAction(self):
        print("V")

    def _deleteNutrientAction(self):
        print("D")

    def _createViewOption(self):
        viewMenu = self.addMenu("&View")
        viewMenu.addAction("Light Mode", self._lightModeAction)
        viewMenu.addAction("Dark Mode", self._darkModeAction)

    def _lightModeAction(self):
        print("G")

    def _darkModeAction(self):
        print("H")

    def _createHelpOption(self):
        helpMenu = self.addMenu("&Help")

