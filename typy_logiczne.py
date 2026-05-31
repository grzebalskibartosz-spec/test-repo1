# from datetime import datetime
#
# x = datetime.now()
# rok = x.year
# miesiac = x.month
# dzien = x.day
# print(f"{dzien}/{miesiac}/{rok}")
#
# data = x.strftime("%d/%m/%Y, %H:%M:%S")
#
# print(data)


# prawda = True
# falsz = False
#
# # Bool mogę uzyskać z wyniku metody
#
# a='ABC'
# sprawdz1 = a.isnumeric()
# sprawdz2= a.islower()
#
# x = 7 > 4
# y = 8 < 4
# z = 10 >= 10
# h = 10 <= 12
# rowne = 'abc' != 'abc'
#
# print(rowne)
#

#
# a = 12
# if a >= 10:
#  print('zgadza się')
# else:
#     print("Liczba jest zamała")

# typ_konta = 'cokolwiek'
#
# if typ_konta == 'admin':
#     print('Witaj w panelu!')
# elif typ_konta == 'mod':
#     print('Witaj moderatorze!')
# else:
#     print('Nie rozpoznano')

# koszyk = 201
# kod = "ABCD"
#
# if koszyk >= 200 and kod == "ABCD":
#     koszyk *=0.9
#     print(f"Uzyskałeś rabat!!! Do zapłaty {koszyk} zł")

# koszyk = 149
# kod = "ABC2026"
# kraj = "PL"
#
# # if koszyk >= 200 and kod == "ABC2026":
# #     koszyk *= 0.9
# #     print(f"Uzyskałeś rabat!!. Do zapłaty {koszyk} zł")
# # else:
# #     print("Nie udało się uzyskać rabatu")
#
# # if koszyk >= 200 and kod == "ABC2026" and kraj == "PL":
# #     koszyk *= 0.9
# #     print(f"Uzyskałeś rabat!!. Do zapłaty {koszyk} zł")
# # else:
# #     print("Nie udało się uzyskać rabatu")
# #
#
# if koszyk > 150 or kod == 'ABC2025':
#     print('Uzyskano rabat')
# else:
#     print('Brak rabatu')

# login = 'admin123'
# dzien = 'sobota'
# aktualizacja = True
#
# if login == 'admin123' and (dzien == 'sobota' or aktualizacja):
#     print('Mozna przeprowadzic aktualizacje')
#
#
# # Do fałszu 0,"",None, [], {}, ()
#
# konwersja = bool(None)
#
# print(konwersja)

#
# zalogowany = True
#
# wiadomosc = 'Witaj w apce' if zalogowany else 'Musisz sie zalogować'
#
# print(wiadomosc)

# from datetime import datetime
#
# month = datetime.now().month
#
# miesiac = None
#
# match (month):
#     case 1:
#         miesiac = "Styczeń"
# case 3:
# miesiac = "marzec"
#


#
# try:
#     print(zmienna)
# except:
#     print('załapałem błąd')
#
# print('aplikacja działa')
#




#
# x=input('Podaj liczbe: ')
#
# try:
#     dzialanie = 100/float(x)
#     if float(x) == 7:
#         raise NameError('Wiadomość błędu')
#     print(dzialanie)
# except ZeroDivisionError as e:
#     print("Nie mozesz dzielic przez 0")
#     print(e)
# except ValueError as e:
#     print("Musisz podać liczbę")
#     print(e)
# except Exception as e:
#     print("Wystapil blad")
#     print(e)

x = input("Podaj liczbę: ")

# ktoś może: dzielić przez 0, brak liczby, nic nie podać
try:
    dzialanie = 100 / float(x)
    if float(x) == 7:
        raise NameError("Wiadomość błędu")
    print(dzialanie)
except ZeroDivisionError as e:
    print("Nie możesz dzielić przez 0!")
    print(e)
except ValueError as e:
    print("Musisz podać liczbę!")
    print(e)
except NameError as e:
    print("Mój własny błąd! Nie można podac liczby 7")
    print(e)
except Exception as e:
    print("Wystąpił błąd")
    print(e)



