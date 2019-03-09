def solution(number):
    i = 1
    sum = 0
    while i < number:
        if i%3 == 0 or i%5 == 0:
            sum += i
        i += 1
    print(sum)
    return sum


def main(args):
    solution(93)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))