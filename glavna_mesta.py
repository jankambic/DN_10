import random

def main():
    drzave_v_mesta = {
        "Slovenija": "Ljubljana",
        "Avstrija": "Dunaj",
        "Italija": "Rim",
    }

    for drzava in drzave_v_mesta:
        random_mesto = random.randint(0, 2)
        drzava = drzave_v_mesta.keys()[random_mesto]
        uganjeno_mesto = raw_input("Katero je glavno mesto drzave " + drzava + ": ")

        preveri(drzava, uganjeno_mesto, drzave_v_mesta)

def preveri(drzava, uganjeno_mesto, drzave_v_mesta):
    dejansko_mesto = drzave_v_mesta[drzava]
    if uganjeno_mesto == dejansko_mesto:
        print("Pravilno")
    else:
        print("Napacno")

if __name__ == '__main__':
    main()