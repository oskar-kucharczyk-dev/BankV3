from datetime import datetime
from konto import Konto
from operacje import znajdz_konto,obsluz_zmiane_hasla,usun_uzytkownika
from historia import historia_operacji
from pliki import wczytaj_konta,zapisz_wszystkie_konta
    

        
        
        





def logowanie(konta):
    login = input("Podaj Login: ")
    konto = znajdz_konto(konta, login)
    haslo = input("Wprowadź hasło: ")
    if konto == None:
        print("Niepoprawny login.")
        return None
    
    if haslo != konto.haslo:
        print("Niepoprawne hasło.")
        return None
    
    return konto

       
        
def menu():
    print("1 -- Sprawdź konto.")
    print("2 -- Wpłać pieniądze.")
    print("3 -- Wypłać pieniądze.")
    print("4 -- Przelew.")
    print("5 -- Zmień login.")
    print("6 -- Zmień hasło.")
    print("7 -- Usuń konto.")
    print("8 -- Wyjście.")



while True:
    konta = wczytaj_konta()
    konto = logowanie(konta)
    if konto == None:
        continue
    
        
    else:
        while True:
            menu()
            try:
             wybor = int(input("Wprowadź operacje którą chcesz wykonać na numpadzie: "))
            except ValueError:
                print("Nieprawidłowa operacja.")
                break
            if wybor == 1:
                konto.pokaz_info()
            elif wybor == 2:
                try:
                    depozyt = int(input("Wprowadź kwotę:"))
                except ValueError:
                    print("Niepoprawna kwota.")
                    break
                if depozyt <= 0:
                    print("Niepoprawna kwota.")
                    break
                else:
                    saldo_przed = konto.saldo
                    konto.wplata(depozyt)
                    zapisz_wszystkie_konta(konta)
                    historia_operacji("WPŁATA",konto,depozyt,saldo_przed)
                    
            elif wybor == 3:
                try:
                    depozyt = int(input("Wprowadź kwotę:"))
                except ValueError:
                    print("Niepoprawna kwota.")
                    break
                if depozyt <= 0:
                    print("Niepoprawna kwota.")
                    break
                saldo_przed = konto.saldo
                wynik = konto.wyplata(depozyt)
                
                if wynik:
                    zapisz_wszystkie_konta(konta)
                    historia_operacji("WYPŁATA",konto,depozyt,saldo_przed)

                if not wynik:
                    print("Operacja się nie udała.")
                    continue
                    
            elif wybor == 8:
                print("Zapraszamy ponownie. ")
                break
            elif wybor == 4:
                login_odbiorca = input("Podaj odbiorcę: ")
                odbiorca = znajdz_konto(konta,login_odbiorca)
                if odbiorca == None:
                    print("Nie znaleziono takiego odbiorcy.")
                    continue
                elif odbiorca == konto:
                    print("Nieprawidłowy odbiorca.")
                    continue
                else:
                    try:
                        kwota = int(input("Podaj kwotę przelewu: "))
                    except ValueError:
                        print("Nieprawidłowa kwota przelewu.")
                        continue
                    if kwota <= 0:
                        print("Nieprawiłowa kwota przelewu.")
                        continue
                    elif kwota > konto.saldo:
                        print("Niewystarczająca ilość środków na koncie.")
                        continue
                    else:
                        saldo_przed = konto.saldo
                        saldo_przed_odbiorcy = odbiorca.saldo
                        konto.przelew(odbiorca,kwota)
                        historia_operacji("PRZELEW_WYSŁANY",konto,kwota,saldo_przed,odbiorca)
                        historia_operacji("PRZELEW_ODEBRANY",odbiorca,kwota,saldo_przed_odbiorcy,konto)
                        zapisz_wszystkie_konta(konta)
            elif wybor == 5:
                stary_login = konto.login
                nowy_login = input("Podaj nowy login:")
                uzyte_loginy = znajdz_konto(konta,nowy_login)
                if uzyte_loginy == None:
                    konto.zmien_login(nowy_login)
                    print("Prosimy zalogować się ponownie.")
                    zapisz_wszystkie_konta(konta)
                    break
                else:
                    print("Przepraszamy, ale podany login jest już używany prosimy o wybranie innego.")
                    continue
            elif wybor == 6:
                wynik = obsluz_zmiane_hasla(konto)
                
                if wynik:
                    print("Hasło zostało zmienione pomyślnie.")
                    zapisz_wszystkie_konta(konta)
                    break
                if wynik == False:
                    print("Haslo niepoprawne.")
                    continue
            elif wybor == 7:
                decyzja = input("Czy napewno chcesz usunąć konto?(TAK/NIE): ")
                if decyzja == "TAK":
                    print("Dobrze, poprosimy cię o podanie hasła w razie bezpieczeństwa.")
                    haslo = input("Wprowadź hasło: ")
                    if haslo != konto.haslo:
                        print("Hasło niepoprawne, w ramach bezpieczeństwa prosimy przeprowadzić całą procedura od nowa.")
                        continue
                    else:
                        wynik = usun_uzytkownika(konta,konto)
                        if wynik:
                            zapisz_wszystkie_konta(konta)
                            print("Hasło poprawne, konto zostało usunięte, dziekujemy za skorzystanie z naszego banku.")
                        if wynik == False:
                            print("Nieudało sie usunąć użytkownika z listy.")
                            
                    
                        break
                elif decyzja == "NIE":
                    print("Powrót do menu...")
                    continue
                else:
                    print("Niewłaściwa decyzja, prosimy o spróbowanie jeszcze raz.")
                    continue
                
            


                



            else:
                print("Nieprawidłowa operacja")
                wybor
            



