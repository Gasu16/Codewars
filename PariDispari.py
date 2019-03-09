def tickets(people):
    i = 0
    # Banconote
    venticinque = []
    cinquanta = []
    cento = []
    Resto = "NO"
    for i in people:
        if i == 25:
            venticinque.append(25)
            # Nessun resto da dare
        if i == 50:
            # Quindi 25 di resto, controllare se ci sono banconote nella lista da 25
            cinquanta.append(50)
            if len(venticinque) > 0:
                #print("Resto disponibile")
                venticinque.remove(25)
                Resto = "YES"
            else:
                #print("Resto NON disponibile")
                Resto = "NO"
            print(50)
        if i == 100:
            cento.append(100)
            if len(venticinque) > 2:
                #print("Resto disponibile")
                venticinque.remove(25)
                venticinque.remove(25)
                venticinque.remove(25)
                Resto = "YES"
            elif (len(cinquanta) > 0 and len(venticinque) > 0):
                venticinque.remove(25)
                cinquanta.remove(50)
            else:
                #print("Resto NON disponibile")
                Resto = "NO"
            print(100)
    return Resto

def main(args):
    return tickets([100])

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))