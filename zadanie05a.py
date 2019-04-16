# Testowanie pierwszej bazy

# Importujemy moduł mysql.connector pod nazwą mysql,
# żeby było krócej i łatwiej niż używanie nazwy mysql.connector
import mysql.connector as mysql


# Łączymy się z serwerem baz danych
moja_baza = mysql.connect(
  host="localhost",
  user="root",
  passwd="haslo"
)

# Ustawiamy obiekt wskaźnika za pomocą którego
# i metody .execute() będziemy wysyłali zapytania
wskaznik = moja_baza.cursor()

# Tworzymy bazę danych o nazwie testowa
# wskaznik.execute("CREATE DATABASE testowa")

# Łączymy się do bazy danych testowa
moja_baza = mysql.connect(
  host="localhost",
  user="root",
  passwd="haslo",
  database="testowa"
)

# Ponownie ustawiamy obiekt wskaźnika
wskaznik = moja_baza.cursor()

# Tworzymy tabelę lista_testowa w bazie testowa
# Tabela bedzie miała trzy pola: id, imie i nazwisko
# id będzie autoinkrementowanym kluczem głównym tabeli
# wskaznik.execute("CREATE TABLE lista_testowa (id INT AUTO_INCREMENT PRIMARY KEY, imie VARCHAR(255), nazwisko VARCHAR(255))")
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
#Procedura listuje dane z bazy
def Lista():
    query= "SELECT * FROM lista_testowa"
    wskaznik.execute(query)
    rows = wskaznik.fetchall()
    print ( "Zestawienie członków Stowarzyszenia. Liczba członków wynosi", wskaznik.rowcount)
    for rekord in rows:
        print(rekord)
#Procedura dopisuje dane do bazy        
def Dopisz():
    Imie =input("Imię: ")
    Nazwisko=input("Nazwisko: ")
    query= "INSERT INTO lista_testowa(imie, nazwisko) VALUES(%s,%s)"
    args=(Imie,Nazwisko)
    wskaznik.execute(query,args)
    print (str(wskaznik.lastrowid))
    print ("Dopisano 1 osobę")
    moja_baza.commit()
#Edycja rekordu w bazie danych
def  Edycja():
    Lista()
    ID = input("Podaj numer danych do edycji: ")
    Imie =input("Imię: ")
    Nazwisko=input("Nazwisko: ")
    query= "UPDATE lista_testowa SET imie=%s, nazwisko=%s WHERE id= %s"
    args=(Imie,Nazwisko,int(ID))
    wskaznik.execute(query,args)
    print (str(wskaznik.lastrowid))
    print ("Zmieniono dane")
    moja_baza.commit()

#Usuwanie rekordu z bazy danych
def  Usun():
    Lista()
    ID = input("Podaj numer danych do usunięcia: ")
    query= "DELETE FROM lista_testowa WHERE id = %s"
    args=(int(ID))
    wskaznik.execute(query,(args,))
    #o co chodzi z tym nawiasem i przecinkiem przy args ????
    print (str(wskaznik.lastrowid))
    print ("Usunięto dane")
    moja_baza.commit()

#Region programu głównego - menu
pozycja_menu = 0
while pozycja_menu != 5:
    pozycja_menu = SprawdzenieLiczby('''
Program prowadzi listę członków stowarzyszenia w oparciu o bazę MySQL:
1 - Lista
2 - Dopisz
3 - Edycja
4 - Usuwanie
5 - Koniec programu
Wybierz polecenie: ''', \
'To nie jest poprawne polecenie.\nWybierz jedną z dostępnych opcji 1 do 5', 1, 5)
    if pozycja_menu == 1:
        Lista()
    elif pozycja_menu == 2:
       Dopisz()
    elif pozycja_menu == 3:
        Edycja()
    elif pozycja_menu == 4:
        Usun()
wskaznik.close()
moja_baza.close()




