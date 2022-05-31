cookbook = {
        "sandwich" : {
            'Ingredients' : ["ham", "bread", "cheese", "tomatoes"], 
            'Meal': 'Lunch', 
            'Prep_time': 10
            },
        "cake" : { 
            "Ingredients" : ["flour", "sugar", "eggs"], 
            "Meal" : "Dessert", 
            "Prep_time": 60
            },
        "salad" : { 
            "Ingredients" : ["avocado", "tomatoes", "spinach"],
            "Meal" : "Lunch",
            "Prep_time": 15
            }
        }
def add_recipe():
    name = input("Please select the recipe:\n")
    try:
        Ingedient_a = str(input("Please enter ingredits:\n"))
        Meal_a= str(input("Please enter meal:\n"))
        time_a= int(input("Please enter time:\n"))
        if time_a <= 0 :
            raise ValueError
    except ValueError:
        print ("Time cannot be 0 or less")
    cookbook[name] = {"Ingedient" : Ingedient_a, "Meal" : Meal_a, "Prep_time" : time_a}

def print_recipe ():
    name = input("Please select the recipe:\n")
    if name in cookbook:
        print("Salad is in the cookbook")
        print(f"Ingredients: {cookbook[name]['Ingredients']}")
        print(f"Meal: {cookbook[name]['Meal']}")
        print(f"Prep_time: {cookbook[name]['Prep_time']}")
    else:
        print("Sorry that option is not int he cookbook")


def delete_recipe():
    name = input("Please select the recipe:\n")
    if name in cookbook:
        del cookbook[name]
    else:
        print("ERROR the name is not in the cookbook")

def print_all():
    print(cookbook)

def ft_exit():
    print("\n\tHope you found what you were looking for, bye !\n")

def select_option(text):
    try:
        loop[text]()
    except:
        print("ERROR option does not exist")


choice = 0
loop = {1 : add_recipe, 2 : delete_recipe, 3 : print_recipe,4 : print_all,  5 : ft_exit}
while (choice != "5"):
    print("Please select an option by typing the corresponding number:")
    choice = input("1.Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n")
    try:
        select_option(int(choice))
    except ValueError:
        print("ERROR Invalid input")
