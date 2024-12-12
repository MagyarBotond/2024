def jelszo():
        
        #Ez a program ellenőrzi, hogy a felhasználó helyesen adja-e meg a jelszavát.
      
        felhasznalonev = "bori99"
        jelszo = "Szivecske"
      
        while True:
          bejelentkezes_felhasznalonev = input("Adja meg a felhasználónevét! ")
          bejelentkezes_jelszo = input("Adja meg a jelszavát! ")
      
          if bejelentkezes_felhasznalonev == felhasznalonev and bejelentkezes_jelszo == jelszo:
            print("Belépés engedélyezve.")
            break
          else:
            print("Belépés megtagadva.")
      
if __name__ == "__main__":
        jelszo()