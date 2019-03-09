def pig_it(text):
    for i, newtext in enumerate(text.split()):
        newtext += newtext[0] + "ay"
        print("".join(newtext[1:]), end = " ")
    #print("".join([newtext[1:] for i in text.split()]))
    return newtext


def main(args):
    pig_it("Pig latin is cool !")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))