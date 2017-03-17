from time import sleep
import pickle


# zapis obiektów do pliku
def plik_zapisz(dane, plik_zapisu):
    plik = open(plik_zapisu, 'wb')
    k = 0
    for i in dane:
        pickle.dump(i, plik)
        k += 1
    plik.close()

# odczyt obiektów z pliku
def plik_czytaj(plik_zapisu):
    plik = open(plik_zapisu, 'rb')
    pickle.load(plik)
    plik.close()


# main
# zapis danych do pliku
dane_1 = [1,2,3,4]
plik_zapisu = 'plik_1.dat'
plik_zapisz(dane_1, plik_zapisu)

# odczyt danych z pliku
plik_czytaj(plik_zapisu)
for i in dane_1:
    print(i)


sleep(2)
