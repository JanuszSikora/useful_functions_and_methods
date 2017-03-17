class Osoba :
    def __init__ (self, imie, nazwisko, login):
        self.imie = imie
        self.nazwisko = nazwisko
        self.login = login

    def __str__(self):
        self.info = self.imie,self.nazwisko,self.login
        return str(self.info)


class Nauczyciel(Osoba):
    def __init__( self,imie, nazwisko):
        super( ).__init__(imie, nazwisko,'brak')

# main
osobaB = Nauczyciel( "Andrzej" , "Andrzejski","andrzeja")
print(osobaB)
osobaB = Nauczyciel( "Andrzej" , "Andrzejski")
print(osobaB)



