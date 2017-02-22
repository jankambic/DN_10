import random

def main():
    skrito_stevilo = random.randint(1, 100)
    ugani_stevilko = int(raw_input("Vpisi iskano stevilko, morda se vam posreci: "))

    while ugani_stevilko != skrito_stevilo:
        ugani_stevilko = raw_input("Prosimo, poskusite ponovno: ")
        if ugani_stevilko == "ne":
            print("Vpisali ste magicno besedo, adijo!")
            break
    else:
        print("Bravo, uspelo vam je!")

if __name__ == '__main__':
    main()