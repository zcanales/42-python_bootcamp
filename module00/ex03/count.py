import sys


def text_analyzer(text = ""):
    idx_upper = 0
    idx_lower = 0
    idx_punt = 0
    idx_space = 0
    ac = len(text)
    if (ac == 0):
       text = input("Please write an text\n")
    """OPCION 1
        text_analyzer(input("Please enter the text to analyze:\n"))"""
    """OPCION 2
     sys.stdout.write("Please write an text\n")
        for line in sys.stdin:
            entry = ""     
      entry += line.rstrip('\n'); #Quitamos el salto de linea"""
    for char in text:
        if (char.isupper()):
            idx_upper += 1
        elif (char.islower()):
            idx_lower += 1
        elif (char.isspace()):
            idx_space += 1
        else:
            idx_punt += 1
    total = idx_punt + idx_space + idx_lower + idx_upper
    print("Total = ", total)
    print("- %d upper letters" % idx_upper)
    print("- %d lower letters" % idx_lower)
    print(f"- {idx_space} space etters")
    print(f"- {idx_punt} punt letters")


argv_len = len(sys.argv) - 1
if (argv_len == 1):
    text_analyzer(sys.argv[1])
else:
    sys.stderr.write("ERROR\n")
