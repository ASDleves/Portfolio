import random


def generalas():
    pakli = []
    szamsor = []
    szamsor.extend(range(2, 11))
    szamsor.extend(['J', 'Q', 'K', 'A'])
    for i in range(4):
        pakli.extend(szamsor)
    return pakli


def huzas(pakli):
    i = random.randint(0, len(pakli) - 1)
    lap = pakli[i]
    pakli.remove(lap)
    return lap


def lapertek(lapok):
    ertek = 0
    aszdarab = 0
    for i in range(len(lapok)):
        if isinstance(lapok[i], int):
            ertek += lapok[i]
        else:
            if 'A' == lapok[i]:
                aszdarab += 1
            else:
                ertek += 10
    if aszdarab > 0:
        for i in range(aszdarab):
            if ertek + 11 <= 21:
                ertek += 11
            else:
                ertek += 1
    return ertek


def jatekkezdes():
    global jatekosmegall
    global gepmegall
    pakli = generalas()
    jatekvege = False
    jatekoslap = []
    geplap = []
    jatekosmegall = False
    gepmegall = False
    for _ in range(2):
        jatekoslap.append(huzas(pakli))
        geplap.append(huzas(pakli))
    while not jatekvege:
        if not jatekvege and not jatekosmegall:
            jatekoskor(jatekoslap, pakli)
        if not jatekvege and not gepmegall:
            gepkor(geplap, pakli)
        if gepmegall and jatekosmegall:
            jatekvege = True
        if jatekvege:
            lapterites(jatekoslap, geplap)
    print()
    ujrakezdes()


def jatekoskor(jatekoslap, pakli):
    global jatekosmegall
    global jatekoserteke
    jatekoserteke = lapertek(jatekoslap)
    print("Játékos köre következik!")
    print("A lapjaid: {}".format(jatekoslap))
    valasz = input("A lapjaid értéke: {}  Szeretnél még húzni? (N/Y): ".format(jatekoserteke))
    valasz = valasz.upper()
    if valasz == "N":
        jatekosmegall = True
        print("Megálltál!")
        print()
    else:
        jatekoslap.append(huzas(pakli))
        jatekoserteke = lapertek(jatekoslap)
        print("A lapjaid: {}".format(jatekoslap))

        if jatekoserteke > 21:
            jatekosmegall = True


def gepkor(geplap, pakli):
    global gepmegall
    global gepertek
    gepertek = lapertek(geplap)
    print("A gép köre következik!")
    if gepertek == 21:
        gepmegall = 1
        print("A gép megállt!")
        print()
        gepmegall = True
    else:
        huzzon_e = random.randint(1, 2)
        while huzzon_e == 1 and gepertek < 21:
            print("A gép lapot húz!")
            geplap.append(huzas(pakli))
            gepertek = lapertek(geplap)
            huzzon_e = random.randint(1, 2)
        print("A gép megállt!")
        print()
        gepmegall = True


def lapterites(jatekoslap, geplap):

    print("Te és a gép is megállt!")
    print("A lapjaid: {} értéke: {}".format(jatekoslap, jatekoserteke))
    print("A gép lapjai: {} értéke: {}".format(geplap, gepertek))
    if 22 > gepertek > jatekoserteke:
        print("A gép nyert!")
    elif 22 > jatekoserteke > gepertek:
        print("Te nyertél!")
    elif jatekoserteke > 21 and gepertek > 21:
        print("Döntetlen, mind a 2 játékos besokalt!")
    elif jatekoserteke == gepertek:
        if len(jatekoslap) > len(geplap):
            print("Te nyertél!")
        elif len(jatekoslap) == len(geplap):
            print("Döntetlen")
        else:
            print("A gép nyert")

def ujrakezdes():
    kerdes = input("Szeretnél még játszani? Y/N: ")
    if kerdes == "Y" or kerdes == "y":
        print()
        jatekkezdes()
