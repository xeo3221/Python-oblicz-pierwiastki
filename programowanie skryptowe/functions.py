from math import sqrt
import matplotlib.pyplot as plt

def oblicz_pierwiastki(*args):
    if len(args) == 3:
        if args[0] == 0 and args[1] == 0 and args[2] == 0:
            print("Funkcja ma nieskończenie wiele rozwiązań.")
            return False
        elif args[0] == 0 and args[1] == 0:
            print("Funkcja nie ma rozwiązań.")
            return False
        elif args[0] == 0:
            x = -args[2] / args[1]
            return (x,)
        else:
            delta = args[1]**2 - 4*args[0]*args[2]
            if delta > 0:
                x1 = (-args[1] + sqrt(delta)) / (2*args[0])
                x2 = (-args[1] - sqrt(delta)) / (2*args[0])
                return (x1, x2)
            elif delta == 0:
                x = -args[1] / (2*args[0])
                return (x,)
            else:
                print("Funkcja nie ma rozwiązań rzeczywistych.")
                return False
    elif len(args) == 2:
        if args[0] == 0:
            print("Funkcja nie ma rozwiązań.")
            return False
        else:
            x = -args[0] / args[1]
            return (x,)
    else:
        print("Niepoprawna liczba argumentów. Funkcja oczekuje 2 lub 3 argumentów.")
        return False

def rysuj_wykres(title, x, y, pierwiastki):
    plt.plot(x, y)
    plt.scatter(pierwiastki, [0] * len(pierwiastki), color='red', label='Pierwiastki')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.grid(True)
    plt.show()