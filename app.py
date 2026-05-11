class Zadanie:
    def __init__(self, nazwa, status, numer=""):
        self.nazwa = nazwa
        self.status = status
        self.numer = numer

    def zadanie_info(self):
        return (
            f"Nr zadania: {self.numer} | Zadanie: {self.nazwa} | Status: {self.status}"
        )


class Lista_Zadań:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.lista_zadan = []

    def dodaj_zadanie(self, nazwa, status):
        numer = len(self.lista_zadan) + 1
        nowe = Zadanie(nazwa, status, numer)
        self.lista_zadan.append(nowe)

    def pokaz_zadania(self):
        for zadanie in self.lista_zadan:
            print(zadanie.zadanie_info)

    def usun_zadanie(self, numer):
        nowa_lista = []
        for zadanie in self.lista_zadan:
            if zadanie.numer != numer:
                nowa_lista.append(zadanie)
        self.lista_zadan = nowa_lista
