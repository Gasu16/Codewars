def polybius(text):
    newtext = ""
    for i in text:
        if i == " ":
            newtext += " "
        if i == "A":
            newtext += "11"
            #print("11")
        if i == "B":
            newtext += "12"
            #print("12")
        if i == "C":
            newtext += "13"
            #print("13")
        if i == "D":
            newtext += "14"
            #print("14")
        if i == "E":
            newtext += "15"
            #print("15")
        if i == "F":
            newtext += "21"
            #print("21")
        if i == "G":
            newtext += "22"
            #print("22")
        if i == "H":
            newtext += "23"
            #print("23")
        if i == "I":
            newtext += "24"
            #print("24")
        if i == "J":
            newtext += "24"
            #print("24")
        if i == "K":
            newtext += "25"
            #print("25")
        if i == "L":
            newtext += "31"
            #print("31")
        if i == "M":
            newtext += "32"
            #print("32")
        if i == "N":
            newtext += "33"
            #print("33")
        if i == "O":
            newtext += "34"
            #print("34")
        if i == "P":
            newtext += "35"
            #print("35")
        if i == "Q":
            newtext += "41"
            #print("41")
        if i == "R":
            newtext += "42"
            #print("42")
        if i == "S":
            newtext += "43"
            #print("43")
        if i == "T":
            newtext += "44"
            #print("44")
        if i == "U":
            newtext += "45"
            #print("45")
        if i == "V":
            newtext += "51"
            #print("51")
        if i == "W":
            newtext += "52"
            #print("52")
        if i == "X":
            newtext += "53"
            #print("53")
        if i == "Y":
            newtext += "54"
            #print("54")
        if i == "Z":
            newtext += "55"
            #print("55")
    print(newtext)
    pass

def main(args):
    polybius("CODEWARS HELLO")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))