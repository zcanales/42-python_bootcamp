import sys


def do_maths(x, y):
    """ This function calculates the four elementary mathematical operations of arithmetic\
    (addition, subtraction, multiplication, division) and the modulo operation."""
    idx_sum = x + y
    idx_res = abs(x - y
    try:
        idx_div = x / y
        idx_mod = x % y
        idx_mul = x * y
    except ZeroDivisionError:
        print("ERROR  Division by zero")
    else:
        print(f"Suma: {idx_sum}")
        print(f"Deferencia: {idx_res}")
        print(f"Division: {idx_div}")
        print("Resta: ", idx_mod)
        print("Division: ", idx_mul)



ac = len(sys.argv)
if (ac != 3):
    sys.stdout.write("Usage: python operations.py <number1> <number2>\n")
else: 
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        do_maths(a, b)
    except ValueError:
        print("ERROR Only numbers")
    """elif (sys.argv[1].isdigit() or sys.argv[2].isdigit()) is False
        sys.stout.write("InputError: only numbers\n")"""
             """if text == 2:
        delete_recipe(input("Please select the recipe:\n"))
    elif text == 3:
        print_recipe(input("Pleas select the recipe:\n"))
    elif text == 5:
        exit()
    else:
        print("This option does not exist")"""
