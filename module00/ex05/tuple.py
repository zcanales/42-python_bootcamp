print("--------TUPLE----------")
print(" 1. OPCION")
tuple2 = (19, 42, 21)
tuple1 = tuple((19, 42, 21))
for x in tuple1:
    print(x)
print("2. OPCION")
for x in range(len(tuple1)):
    print(tuple1[x])
print("3. OPCION")
i = 0
while i < len(tuple1):
    print(tuple1[i])
    i += 1
print("4. OPCION")
print(tuple1[:])
print("5. OPCION")
print(f"{tuple1[:]}")
print(type(tuple1))
print(type(tuple2))
