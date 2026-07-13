from konto import Konto
def znajdz_konto(konta, login):
    for konto in konta:
        if konto.login == login:
            return konto
    return None
def najbogatszy_klient(konta):
    najbogatszy = konta[0]
    for konto in konta:
        if konto.saldo > najbogatszy.saldo:
            najbogatszy = konto
    return najbogatszy
def usun_uzytkownika(konta,uzytkownik):
    if uzytkownik in konta:
        konta.remove(uzytkownik)
        return True
    
    return False
def obsluz_zmiane_hasla(konto):
    stare_haslo = input("Wprowadź stare hasło: ")
    while True:
        nowe_haslo = input("Wprowadź nowe hasło: ")
        nowe_haslo_sprawdzenie = input("Wprowadź nowe hasło jeszcze raz: ")
        if len(nowe_haslo) < 6:
            print("Hasło musi się składać z 6 znaków: ")
            continue
        elif nowe_haslo != nowe_haslo_sprawdzenie:
            print("Hasła nie są takie same.")
            continue
        wynik = konto.zmien_haslo(stare_haslo,nowe_haslo)
        if wynik:
            print("Hasło zostało zmienione pomyślnie.")
            return True
        
        print("Stare hasło jest niepoprawne.")
        return False

    
        
        
