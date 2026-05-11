from zadanie import Zadanie
from lista_zadan import Lista_Zadań


def menu(lista_zadan):
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
            if not lista_zadan.lista_zadan:
                print("Brak zadań na liscie")
            else:
                lista_zadan.pokaz_zadania()
        elif choice == 2:
            nazwa = input("Zadanie: ")
            while True:
                print("\n--- Wybierz status ---")
                print("1. Do zrobinia")
                print("2. Zrobione")
                print("3. Cofnij")

                try:
                    choice = int(input("Wybierz: "))
                except ValueError:
                    print("Tylko cyfry")
                    continue

                if choice == 1:
                    lista_zadan.dodaj_zadanie(nazwa, status="Do zrobienia")
                    break
                elif choice == 2:
                    lista_zadan.dodaj_zadanie(nazwa, status="Zrobione")
                    break
                elif choice == 3:
                    print("Cofanie...")
                    break
                else:
                    print("Tylko cyfrey 1-5")
                    continue

        elif choice == 3:
            try:
                choice = int(input("Usuń zadanie nr: "))
            except ValueError:
                print("Tylko cyfry")
                continue

            zadanie_istnieje = False
            for nr in lista_zadan.lista_zadan:
                if choice == nr.numer:
                    zadanie_istnieje = True
                    break
            if zadanie_istnieje:
                lista_zadan.usun_zadanie(choice)
                print(f"\nZadanie nr: {choice} zostało usunięte")
                continue
            else:
                print("Nie ma takiego zadani")
                continue
        elif choice == 4:
            if not lista_zadan.lista_zadan:
                print("Brak zadań na liscie")
            else:
                try:
                    choice = int(input("Nr zadania: "))
                except ValueError:
                    print("Tylko cyfry")
                    continue

                zadanie_istnieje = False
                for nr in lista_zadan.lista_zadan:
                    if choice == nr.numer:
                        zad = nr
                        zadanie_istnieje = True
                        break

                if zadanie_istnieje:
                    print(f"\n--- Zmiana statusu ---")
                    print("1. Do zrobienia")
                    print("2. Wykonane")
                    print("3. Cofnij")

                    try:
                        choice = int(input("Wybierz: "))
                    except ValueError:
                        print("Tylko cyfry")
                        continue

                    if choice == 1:
                        zad.zmien_status("Do zrobienia")
                    elif choice == 2:
                        zad.zmien_status("Wykonane")
                    elif choice == 3:
                        print("Cofanie...")
                        break
                    else:
                        print("Tylko cyfry 1-3")
                        continue
                else:
                    print("Brak takiego zadani na liscie!")
                    continue

        elif choice == 5:
            print("Zamykanie")
            break
        else:
            print("Tylko cyfrey 1-5")
            continue


lista_zadan = Lista_Zadań("Lista ToDo")

menu(lista_zadan)
