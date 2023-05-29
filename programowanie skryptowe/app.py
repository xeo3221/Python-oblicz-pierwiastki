import numpy as np
from functions import oblicz_pierwiastki, rysuj_wykres

wyniki = {
    'kwadratowa': [],
    'liniowa': []
}

start = True
while start:
    funkcja = input("Wybierz rodzaj funkcji:\n1. Funkcja kwadratowa\n2. Funkcja liniowa\n3. Koniec\n").lower()

    if funkcja == '1' or funkcja == 'funkcja kwadratowa':
        try:
            a = float(input("Podaj współczynnik a: "))
            b = float(input("Podaj współczynnik b: "))
            c = float(input("Podaj współczynnik c: "))
        except ValueError:
            print("Niepoprawne dane. Podaj liczbę.")
        pierwiastki = oblicz_pierwiastki(a, b, c)
        if pierwiastki:
            print(f'Pierwiastki funkcji kwadratowej: {pierwiastki}')
            wyniki['kwadratowa'].append(pierwiastki)
            x = np.linspace(-10, 10, 100)
            y = a * x**2 + b * x + c
            rysuj_wykres(f'Funkcja kwadratowa: {a}x^2 + {b}x + {c}', x, y, pierwiastki)

    elif funkcja == '2' or funkcja == 'funkcja liniowa':
        try:
            a = float(input("Podaj współczynnik a: "))
            b = float(input("Podaj współczynnik b: "))
        except ValueError:
            print("Niepoprawne dane. Podaj liczbę.")
        pierwiastki = oblicz_pierwiastki(a, b)
        if pierwiastki:
            print(f'Pierwiastki funkcji liniowej: {pierwiastki}')
            wyniki['liniowa'].append(pierwiastki)
            x = np.linspace(-10, 10, 100)
            y = a * x + b
            rysuj_wykres(f'Funkcja liniowa: {a}x + {b}', x, y, pierwiastki)

    elif funkcja == 'koniec' or funkcja == '3':
        start = False

print(f'Wyniki: {wyniki}')

with open('wyniki.txt', 'w', encoding='utf-8') as file:
    file.write('Wynik z programu: \n')
    for key in wyniki.keys():
        for value in wyniki[key]:
            if key == 'kwadratowa':
                file.write(f'Funkcja {key} {a}x^2 + {b}x + {c}:  {value} \n')
            else:
                file.write(f'Funkcja {key} {a}x + {b}:  {value} \n')