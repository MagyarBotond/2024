def óraperc(perc): # Egésztse ki a függvénydefiníciót paraméterrel!
        óra = perc // 60 # Írja meg a függvény többi részét!
        perc = perc % 60
        return str(óra) + ' óra ' + str(perc) + ' perc'
    
film_lista = []
    
while True:
        film_cim = input("Add meg egy film címét! ")
        perc = int(input("Hány perces a film? "))
        film_lista.append((film_cim, perc))
        if len(film_lista) == 3:
            break
    
for film_cim, perc in film_lista:
        ora_perc = óraperc(perc)
        print(f"A(z) {film_cim} című film {ora_perc} hosszú.")