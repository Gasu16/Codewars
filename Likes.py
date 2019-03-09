def valid_parentheses(string):
    count1 = string.count('(') # Contiamo le parentesi aperte (
    count2 = string.count(')') # Contiamo le parentesi chiuse )
    if count1 == count2:
        return True
    else:
        return False


def main(args):
    print(valid_parentheses(")kucn(lmzqekvhrbjla(rgmxcumr)t)p(et"))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))