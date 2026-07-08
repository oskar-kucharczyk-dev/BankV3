
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