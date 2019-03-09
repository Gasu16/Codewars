def increment_string(strng):
    for i in strng:
        if i.isdigit():
            oldi = i
            newi = int(i)+1
        strng = strng.replace(oldi, str(newi))
    print(strng)
    return strng

def main(args):
    increment_string("foobar29")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))