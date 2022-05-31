class Recipe:
    name = ''
    cooking_lvl = 0
    cooking_time = 0
    ingredients = []
    description = '' 
    recipe_type = ''
    def __init__(self, name = None, cooking_lvl = None,cooking_time = None, ingredients = None, description = None, recipe_type = None):
        print("Recipe constructor called")
        try:
            self.name = str(name)
            self.cooking_lvl = int(cooking_lvl)
            self.cooking_time = int(cooking_time)
            self.ingredients = str(ingredients)
            self.description = str(description)
            self.recipe_type = str(recipe_type)
            if name is None:
                raise Exception("Name empty")
            if cooking_lvl > 5 or cooking_time < 1:
                raise Exception("Invalid cooking time range 1 - 5")
            if cooking_time < 0 :
                raise Exception("Negative number")
            if recipe_type not in ['lunch', 'starter', 'dessert']:
                raise Exception("Invalid recipe type")
        except (Exception , ValueError) as e:
            print("Recy exception raised: ", repr(e))
            exit()
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "Name: " + self.name + ". Cooking_lvl: " + str(self.cooking_lvl) + ". Cooking_time: " + str(self.cooking_time) + ". Ingredient: " + self.ingredients + ". Description: " + self.description + ". Recipe_type: " + self.recipe_type
        return txt

b = Recipe("Btest", 1, 10, ["Avocat", "Mayonnaise"], "", "starter")
print(str(b))
