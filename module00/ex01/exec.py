import sys
parameter = sys.argv
idx = len(parameter)
print("Parameter len: ", idx, "\nParamter are: ", parameter)
i = 1
string = ''
while i < idx:
    j = 0;
    while (j < len(parameter[i])):
        if parameter[i][j].isupper():
            string += parameter[i][j].lower()
        else:
            string += parameter[i][j].upper()
        j += 1
    i += 1
txt = string [::-1]
print(txt, end=" ")
