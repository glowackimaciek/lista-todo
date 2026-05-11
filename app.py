class Zadanie:
    def __init__(self, nazwa, status, numer):
        self.nazwa = nazwa
        self.status = status
        self.numer = numer

    def zadanie_info(self):
        return (
            f"Nr zadania: {self.numer} | Zadanie: {self.nazwa} | Status: {self.status}"
        )
