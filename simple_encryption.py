def decrypt(text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i + 1] + a[i:i + 1] for i in range(ndx + 1))
    return text


def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text

def main(args):
    print(encrypt("This is a test!", 1))
    print(decrypt("hsi  etTi sats!", 1))
    #encrypt("", 1)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))