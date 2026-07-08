from datetime import datetime
def historia_operacji(operacja,konto,kwota,saldo_przed,drugi_uzytkownik=None):
    czas = datetime.now()
   
    with open("historia.txt","a",encoding="utf-8") as file:
        if operacja == "WPŁATA":
            file.write(f"{czas.strftime('%Y.%d.%m')}--{operacja}--{konto.login}--{kwota}--{saldo_przed}--{konto.saldo}" + "\n")
        elif operacja == "WYPŁATA":
            file.write(f"{czas.strftime('%Y.%d.%m')}--{operacja}--{konto.login}--{kwota}--{saldo_przed}--{konto.saldo}" + "\n")
        elif operacja == "PRZELEW_WYSŁANY":
                file.write(f"{czas.strftime('%Y.%d.%m')}--{operacja}--{konto.login}--{drugi_uzytkownik.login}--{kwota}--{saldo_przed}--{konto.saldo}" + "\n")
        elif operacja == "PRZELEW_ODEBRANY":
                file.write(f"{czas.strftime('%Y.%d.%m')}--{operacja}--{konto.login}--{drugi_uzytkownik.login}--{kwota}--{saldo_przed}--{konto.saldo}" + "\n")