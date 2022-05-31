import time
from recipe import Recipe

class Book:
    last_update  = time.time()
    creation_date = time.time()
    def __init__(self, name):
        self.name = name
        self.recipe_list = {"starter" : [], "lunch" : [], "dessert": []}
        print("Book constructor called")
    def __str__(self):
        txt = ("Recipe book's name : " + self.name + "\n"
                + "Last update : " + str(self.last_update) + "\n"
                + "Creation date : " + str(self.creation_date) + "\n"
                + "Starters : " + str(self.recipe_list['starter']) + "\n"
                + "Lunches : " + str(self.recipe_list['lunch']) + "\n"
                + "Desserts : " + str(self.recipe_list['dessert']))
        return txt
    def  get_recipe_by_name(self, name):
        """Print a recipe with the name 'name' and return the instance"""
        print(f"Name: {name}")
        return self
   
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_types"""
        for i in self.recipe_list.keys():
            if i is recipe_type:
                return(print(self.recipe_list[i]))
        print("That recipe type is not in the book")

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe):
            if recipe.recipe_type in self.recipe_list:
                self.recipe_list[recipe.recipe_type].append(recipe)
                self.last_update =  time.time()
                return
            else:
                print("Error: Recipe type is not satart, lunch or dessert")
        else:
            print("This recipe is not a Recipe class")

b = Book("Bibi")
