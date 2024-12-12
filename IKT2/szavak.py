a = input("Adj meg egy szót! ")
b = input("Adj meg egy másik szót! ")
l1, l2 = len(a), len(b)

if l1 == l2:
    print("Két szó egyforma hosszú")
else:
    print(f"A hosszabb szó: {max(a, b, key=len)}")