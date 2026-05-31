
imie = 'Bartosz'
nazwisko = 'Grzebalski'
miasto = 'Warszawa'
zdanie1 = f'To jest {imie} {nazwisko}. Jego miejsce urodzenia to {miasto}'
print(zdanie1)

result = 'to jest krótkie zdanie na temat Bartisza'
zdanie2 = result.replace(""' ', '-')
print(zdanie2)

greeting = 'hello world'
dlugosc_str = len(greeting)
print(dlugosc_str)
duze_litery = greeting.upper()
print(duze_litery)
pierwsza_duza_litera = greeting.capitalize()
print(pierwsza_duza_litera)

movie = "lord of the rings"
pierwsze_duze=movie.title()
print(pierwsze_duze)

movie = "dzisiaj jest sobota"
znajdz_piatke = movie[4]
print(znajdz_piatke)