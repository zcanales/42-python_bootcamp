import sys

def check(number):
    if (number == 0):
        sys.stdout.write("I'm Zero \n")
    elif (number % 2):
        sys.stdout.write("I'm Odd\n")
    else:
        sys.stdout.write("I'm Even\n")

av = sys.argv
ac = len(av)
if (ac != 2):
    print("ERROR")
    sys.exit()
if (av[1].isdigit()):
    check(int(av[1]))
else:
    sys.stdout.write("ERROR\n")
    sys.exit()

