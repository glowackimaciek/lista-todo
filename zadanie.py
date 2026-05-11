class Zadanie:
    def __init__(self, nazwa="", status="", numer=""):
        self.nazwa = nazwa
        self.status = status
        self.numer = numer

    def zmien_status(self, nowy_status):
        self.status = nowy_status

    def zadanie_info(self):
        return (
            f"Nr zadania: {self.numer} | Zadanie: {self.nazwa} | Status: {self.status}"
        )
