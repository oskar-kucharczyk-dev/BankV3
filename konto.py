class Konto:
    def __init__(self,login,haslo,saldo):
        self.login = login
        self.haslo = haslo
        self.saldo = saldo
    def pokaz_saldo(self):
        return f"Saldo użytkownia {self.login} wynosi {self.saldo} zł" 
    def wplata(self, wplata):
        self.saldo += wplata
        print(f"Nowe saldo konta po wpłacie {wplata} zł to {self.saldo} zł")
    def wyplata(self, wyplata):
        if wyplata > self.saldo:
            print("Nie wystarczająca ilość środków na koncie.")
            return False
        
        self.saldo -= wyplata
        print(f"Nowe saldo konta po wypłacie {wyplata} zł to {self.saldo} zł")
        return True
    
    def przelew(self, uzytkownik,kwota):
        if kwota > self.saldo:
            print("Nie wystarczająca kwota na przelew środków.")
        else:
            self.saldo -= kwota
            uzytkownik.saldo += kwota
            print(f"Pomyślnie przelano {kwota} zł na konto {uzytkownik.login}.")
    def zmien_login(self,nowylogin):
        starylogin = self.login
        self.login = nowylogin

        
        print(f"Pomyślnie zmieniono login z {starylogin} na {nowylogin}")
    
    def pokaz_info(self):
        print(f"Login: {self.login}")
        print(f"Saldo: {self.saldo}")
    
    def kredyt(self):
        if self.saldo <= 1000:
            print("nie możemy udzielić państwu kredytu")
        else:
            print("Możemy udzielić państwu kredyt.")

    def pobierz_login(self):
        return self.login
    
    def czy_bogaty(self):
        if self.saldo >= 1000:
            return "bogaty klient"
        else:
            ile_brakuje = 1000 - self.saldo
            return f"Nie bogaty klient do 1000 brakuje {ile_brakuje} zł. "
    #konto.py
    def porownanie_salda(self, uzytkownik):
        uzytkownik.saldo
        if self.saldo > uzytkownik.saldo:
            return f"{self.login} Jest bogatszy od {uzytkownik.login}"
        elif self.saldo == uzytkownik.saldo:
            return f"{self.login} jest tak samo bogaty z {uzytkownik.login}"
        else:
            return f"{self.login} jest biedniejszy od {uzytkownik.login}"
    def zmien_haslo(self,stare_haslo,nowe_haslo):
        if stare_haslo != self.haslo:
            return False
            

        self.haslo = nowe_haslo
        return True
    
    