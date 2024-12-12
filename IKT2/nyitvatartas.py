t = int(input("Hány óra van most? "))

if 8 <= t <= 16:
    print("A bolt nyitva van.")
    print(f"Ennyi órád van még oda érni: {16 - t}")
else:
    print("A bolt zárva van ")