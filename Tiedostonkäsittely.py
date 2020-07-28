#  Tee ohjelma joka, lukee sanoja tiedostosta rivi kerrallaan
#  1. Jokainen sana on omalla rivillään, joten 1 rivi == 1 sana
#  2. Järjestää sanat järjestykseen ensisijaisesti pituuden ja toissijaisesti aakkosjärjestyksen mukaan
#  3. Kirjoittaa järjestetyt sanat toiseen tiedostoon
#  4. Ohjelma ei saa kaatua vaikka tiedostonkäsittelyssä olisi virheitä (try/except)


try:

    with open('C:\\Users\\Kati\\Desktop\\testi.txt') as tiedosto:
        rivit = tiedosto.readlines()
        lista = []

        for i in rivit:
            lista.append(i.strip('\n'))
        lista.sort(key=lambda x: (-len(x), x))

        print(lista)
        lista2 = '\n'.join(lista)

        with open('C:\\Users\\Kati\\Desktop\\testi2.txt', 'w') as tiedosto2:
            tiedosto2.write(lista2)
except OSError as err:
    print('System related error')
except:
    print("Unexpected error occurred")

