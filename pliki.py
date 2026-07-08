from konto import Konto
def wczytaj_konta():
    konta = []

    with open("konta.txt", "r", encoding="utf-8") as file:
        for linia in file:
            if linia.strip() == "":
                continue

            czesci = linia.strip().split("--")
            login = czesci[0]
            haslo = czesci[1]
            saldo = int(czesci[2])

            konto = Konto(login,haslo,saldo)
            konta.append(konto)

    return konta
def zapisz_wszystkie_konta(konta):
    with open("konta.txt","w",encoding="utf-8") as file:
        for konto in konta:
            file.write(f"{konto.login}--{konto.haslo}--{konto.saldo}"+ "\n")