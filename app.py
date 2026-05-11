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


def menu(lista_zadan, zadanie):
    while True:
        print(f"\n--- {lista_zadan.nazwa} ---")
        print("1. Wyświetl zadania")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        print("4. Zmień status zadania")
        print("5. Zamknij")

        try:
            choice = int(input("Wybierz: "))
        except ValueError:
            print("Tylko cyfry")
            continue

        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            print("Zamykanie")
            break
        else:
            print("Tylko cyfrey 1-5")
            continue


lista_zadan = Lista_Zadań("Lista ToDo")
zadanie = Zadanie()

menu(lista_zadan, zadanie)
