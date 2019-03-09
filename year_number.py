def distinct_year_digits(year):
    year += 1
    sy = str(year)
    sety = set(sy)
    l1 = len(sety)
    l2 = len(sy)
    if l1 == l2:
        return year

    return distinct_year_digits(year)

def main(args):
    print(distinct_year_digits(2029))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))