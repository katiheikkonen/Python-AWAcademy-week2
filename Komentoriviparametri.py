#  tehtävän kolme koodi, mutta komentoriviparametrilla

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('string', metavar='N', type=str,
                    help='an integer for the accumulator')

args = parser.parse_args()
print(args.string)

try:

    with open(args.string) as tiedosto:
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
