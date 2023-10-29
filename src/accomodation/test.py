import sys
from model import Accommodation, Hotels


def main():
    n = int(sys.argv[1] if len(sys.argv) > 1 else 0)
    if n <= 0:
        raise ValueError("Nincs argumentum")

    list = []
    for _ in range(n):
        line = input()
        tokens = line.split(";")
        name = tokens[0]
        city = tokens[1]
        price = tokens[2]

        if len(tokens) == 3:
            acc = Accommodation(name, int(price), city)
            list.append(acc)
        else:
            stars = tokens[3]
            hotel = Hotels(name, city, int(price), int(stars))
            list.append(hotel)

    list.sort()
    for accom in list:
        print(accom)


if __name__ == '__main__':
    main()
