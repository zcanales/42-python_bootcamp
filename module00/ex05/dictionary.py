print("--------DICTIONARY----------")
dict1 = {"Phyton": "Guidos van Rosuum", "Ruby" : "Ykihiro Matsumoto"}
print(" 1. OPCION")
print(dict1)
print(" 2. OPCION")
print(f"{dict1}")
print(" 3. OPCION")
print(dict1.keys())
print(dict1.values())
print(dict1.items())
if "Phyton" in dict1:
    print(type(dict1))
print(" 4. OPCION")
for x , y in dict1.items():
    print(x, y)
