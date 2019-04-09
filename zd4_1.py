


# AppHS
# Aplikacja prowadzi rejestr członków stowarzyszenia Hackerspace
# Zadanie polegało na zmianie indeksowania

# ******** FUNKCJE ********

# Funkcja sprawdzająca poprawność wprowadzonego tekstu i zwracająca poprawny tekst
def SprawdzenieTekstu(typ, tekst_zachety, komunikat_bledu):
    tekst_do_sprawdzenia = ''
    while not tekst_do_sprawdzenia.isalpha():
        tekst = input(tekst_zachety)
        if typ == 'proste':
            tekst_do_sprawdzenia = tekst
        elif typ == 'złożone':
            tekst_do_sprawdzenia = tekst.replace(' ', '')
            tekst_do_sprawdzenia = tekst_do_sprawdzenia.replace('-', '')
        if not tekst_do_sprawdzenia.isalpha():
            print(komunikat_bledu)
    return tekst

# Funkcja sprawdzająca poprawność wprowadzonej liczby i zwracająca poprawnę liczbę
def SprawdzenieLiczby(tekst_zachety, komunikat_bledu, dolna_granica, gorna_granica):
    liczba = ''
    while not liczba.isdigit():
        liczba = input(tekst_zachety)
        if not liczba.isdigit():
            print(komunikat_bledu)
            liczba = ''
        elif not int(liczba) in range(dolna_granica, gorna_granica + 1):
            print(komunikat_bledu)
            liczba = ''
    return int(liczba)
# Funkcja sprawdza index osoby wpisanej w ostatnij linii danych pliku.
def NowyNumer():
    import os
    CzyJestPlik=os.path.isfile('lista_czlonkow.txt')
    if CzyJestPlik == False:
        IndeX="0"
        return int(IndeX)
    csvfile = open('lista_czlonkow.txt').readlines()
    array=[]
    for line in csvfile:
        array.append(line)
    ostLn = array[-1].split()
    IdX = ostLn[0].replace("[","")
    IndeX = IdX.replace(",","")
    return int(IndeX)
# ******** PROCEDURY ********

# Procedura wyświetlająca listę członków stowarzyszenia
def ListaCzlonkow():
    lista_czlonkow = open('lista_czlonkow.txt').read()
    print('Lista członków stowarzyszenia: ')
    print(open('lista_czlonkow.txt').read())

# Procedura dodająca członków stowarzyszenia do pliku lista_czlonków.txt i wyświetlająca dane każdego dodanego członka
def DodawanieCzlonkow():
    ilosc_dodawanych_czlonkow = SprawdzenieLiczby('Podaj ilu członków dodajesz do listy: ', \
                                                'To nie jest poprawna liczba członków.\nWprowadź liczbę od 1 do 10.', 1, 10)
    for n in range(ilosc_dodawanych_czlonkow):
        imie_czlonka = SprawdzenieTekstu('proste', 'Podaj imię: ', \
                                        'To nie jest poprawne imię!\nPoprawne imię składa się wyłącznie z liter.')
        nazwisko_czlonka = SprawdzenieTekstu('złożone', 'Podaj nazwisko: ', \
                                            'To nie jest poprawne nazwisko!\nPoprawne nazwisko składa sie wyłącznie z liter spacji i myślników.')
        rok_urodzenia = SprawdzenieLiczby('Podaj rok urodzenia: ', \
                                        'Musisz podać rok pomiędzy 1880 a obecnym.', 1880, teraz.year)
        wiek = teraz.year - rok_urodzenia
        nastepny = NowyNumer() + 1
        nowy = [nastepny, imie_czlonka, nazwisko_czlonka, rok_urodzenia]
        #nowy = [n + 1, imie_czlonka, nazwisko_czlonka, rok_urodzenia]
        lista_czlonkow = open('lista_czlonkow.txt', 'a')
        #lista_czlonkow
        lista_czlonkow.write(str(nowy) + '\n')
        lista_czlonkow.close()
        print('Dodano:\n' + imie_czlonka, nazwisko_czlonka + '\nRok urodzenia:', rok_urodzenia, 'Wiek:', wiek)
# Procedura usuwająca członków stowarzyszenia z pliku lista_czlonków.txt i wyświetlająca dane przed i po usunieciu
def  UsuwanieCzlonkow():

    ListaCzlonkow()
    ileWierszy=NowyNumer()
    IdXOsoby = SprawdzenieLiczby('Wybierz numer osoby do skreślenia z listy: ' ,\
                      'Musisz podać liczbę z wskazanego zakresu.', 0, ileWierszy)
    csvfile = open('lista_czlonkow.txt').readlines()
    array=[]
    Id = '[' + str(IdXOsoby)
    bUsun=False
    for line in csvfile:
        if not line.startswith(Id):
            array.append(line)
        if line.startswith(Id):
            bUsun=True
        
    if bUsun:
            print ('Dane zostały usunięte ')
    else:
            print ('Nie znaleziono danych o takim numerze - ')        
    csvfile=open('lista_czlonkow.txt','w')
    csvfile.writelines(array)
# Procedura edycja danych o członkach stowarzyszenia z pliku lista_czlonków.txt 
def EdycjaDanych():
    ListaCzlonkow()
    ileWierszy=NowyNumer()
    IdXOsoby = SprawdzenieLiczby('Wybierz numer wiersza do edycji: ' ,\
                      'Musisz podać liczbę z wskazanego zakresu.', 0, ileWierszy)
    csvfile = open('lista_czlonkow.txt').readlines()    
    array=[]
    Id = '[' + str(IdXOsoby)
    
    #Czyszczenie pliku
    delFile=open('lista_czlonkow.txt','w')
    for line in csvfile:
        if line.startswith(Id):           
            imie_czlonka = SprawdzenieTekstu('proste', 'Podaj imię: ', \
                                        'To nie jest poprawne imię!\nPoprawne imię składa się wyłącznie z liter.')
            nazwisko_czlonka = SprawdzenieTekstu('złożone', 'Podaj nazwisko: ', \
                                            'To nie jest poprawne nazwisko!\nPoprawne nazwisko składa sie wyłącznie z liter spacji i myślników.')
            rok_urodzenia = SprawdzenieLiczby('Podaj rok urodzenia: ', \
                                        'Musisz podać rok pomiędzy 1880 a obecnym.', 1880, teraz.year)
            wiek = teraz.year - rok_urodzenia
            nowy = [IdXOsoby, imie_czlonka, nazwisko_czlonka, rok_urodzenia]
            #array.append(nowy)
            csvfile=open('lista_czlonkow.txt','a')
            csvfile.write(str(nowy) + '\n')
        else:
            csvfile=open('lista_czlonkow.txt','a')
            csvfile.write(str(line))    
    
# ******** GŁÓWNY PROGRAM ********

# Pobranie aktualnej daty i czasu
import datetime
teraz = datetime.datetime.now()

# Menu główne
pozycja_menu = 0
while pozycja_menu != 5:
    pozycja_menu = SprawdzenieLiczby('''1 - Lista członków stowarzyszenia
2 - Dodanie nowych danych
3 - Usuwanie członka stowarzyszenia
4 - Edycja danych osobowych
5 - Koniec programu
Wybierz polecenie: ''', \
'To nie jest poprawne polecenie.\nWybierz jedną z dostępnych opcji 1 do 5', 1, 5)
    if pozycja_menu == 1:
        ListaCzlonkow()
    elif pozycja_menu == 2:
        DodawanieCzlonkow()
    elif pozycja_menu == 3:
        UsuwanieCzlonkow()
    elif pozycja_menu == 4:
        EdycjaDanych()
        

# Koniec
input('Aby zakończyć naciśnij klawisz ENTER.')
