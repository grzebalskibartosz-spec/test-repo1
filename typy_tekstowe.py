# # str - string
#
# # typ porsty prymitywny
#
# miasto = "Katowice"
# nazwisko = 'Kowalski'
#
# sprawdz_typ = type(miasto)
#
# print(sprawdz_typ)
#
# # konkatenacja
#
# jezyk = "Python"
# typ_jezyka = "backendowy"
#
# zdanie = jezyk + " to popularny język programowania"
# zdanie2 = "Mój ulubiony język to " + jezyk + ". Jest on " + typ_jezyka + "."
#
# zdanie3 = f"Mój ulubiony język to {jezyk}. Jest on {typ_jezyka}."
#
# print(zdanie2)
# print(zdanie3)


film = 'haRRy pOtTer'

duza_litera = film.upper()
tytul = film.title()
zastap_znaki = film.replace('R',"_")

film = "haRRy pOtTer: Zakon Feniksa"

duza_litera = film.upper()
tytul = film.title()
zastap_znaki = tytul.replace("r","_")
zastap_fraze = film.replace("Zakon Feniksa", "Czara Ognia")

policz = film.count("R")
policz_bez_czulosci_na_litery = film.lower().count("r")

print(duza_litera)
print(tytul)
print(zastap_znaki)

akapit = 'To jest mój tekst'
pierwsza_litera = akapit[0]
ostatnia_litera = akapit[-1]
fragment = akapit[0:7]

rozpocznij_od = akapit[5::]

print(rozpocznij_od)
print(fragment)
print(ostatnia_litera)