

def borton():

    cellak = {}
    for x in range(100):
        cellak["Cella{0}".format(x+1)] = "Zarva"
    cella_szamlalo = 1
    cellaszam = 1
    for f in range(100):
        for k in range(100):
            if cellaszam % cella_szamlalo == 0:
                if cellak["Cella{0}".format(k+1)] == "Zarva":
                    cellak["Cella{0}".format(k+1)] = "Nyitva"
                else:
                    cellak["Cella{0}".format(k+1)] = "Zarva"
            cellaszam += 1
        cellaszam = 1
        cella_szamlalo += 1
    for p in range(100):
        print("A {} cella ".format(p+1),cellak["Cella{0}".format(p+1)])
borton()