import sys


def check(message, code=1):
    print(message)
    sys.exit(code)


def func_cipher(k):
    # Text to cipher
    text = input("plaintext:  ")

    # Alphabet to be used
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case = "abcdefghijklmnopqrstuvwxyz"

    # Encrypted chain.
    cipher = ""

    # Make cipher.
    for c in text:
        if c in upper_case:
            cipher += upper_case[(upper_case.index(c) + k) % len(upper_case)]
        elif c in lower_case:
            cipher += lower_case[(lower_case.index(c) + k) % len(lower_case)]
        else:
            cipher += c

    # Visualize final text.
    print("ciphertext: ", cipher)


if len(sys.argv) != 2:
    check("Usage: python caesar.py k, where k is the offset number")
else:
    # Shift value
    script, val = sys.argv
    num = abs(int(val))
    func_cipher(num)