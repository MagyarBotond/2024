def sikeres_vizsga(pont):
        """
        A függvény eldönti, hogy a vizsga sikeres-e.
      
        Args:
          pont: A vizsgázó által elért pontszám.
      
        Returns:
          True, ha a vizsga sikeres, False, ha nem.
        """
        return pont >= 48
      
while True:
        nev = input("Add meg a vizsgázó nevét! ")
        if nev == "":
          break
        pont = int(input("Add meg a pontszámát! "))
        if sikeres_vizsga(pont):
          print(f"{nev} vizsgája sikeres.")
        else:
          print(f"{nev} vizsgája sikertelen.")