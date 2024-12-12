n = int(input("Hány órás visszaszámlálást tervezünk? "))
h = 0

while n > 0:
    k = input("Fel kell függeszteni a visszaszámlálást (i/n)? ")

    if k == "i":
        h += 1

    print(f"Visszaszámlálás: {n}")

    h += 1
    n -= 1

print(f"A rakéta visszaszámlálást követően ennyi órával indult: {h}")