from Crypto.Util import number
import random


def generateKeys(keysize=1024):
    e = d = N = 0

    # get prime nums, p & q
    p = number.getPrime(keysize)
    q = number.getPrime(keysize)

    print(f"p: {p}")
    print(f"q: {q}")

    N = p * q  # RSA Modulus
    phiN = (p - 1) * (q - 1)  # totient

    # choose e
    # e is coprime with phiN & 1 < e <= phiN
    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if isCoPrime(e, phiN):
            break

    # choose d
    # d is mod inv of e with respect to phiN, e * d (mod phiN) = 1
    d = modularInv(e, phiN)

    return e, d, N


# return True if gcd(p, q) is 1
def isCoPrime(p, q):
    return gcd(p, q) == 1


# euclidean algorithm to find gcd of p and q
def gcd(p, q):
    while q:
        p, q = q, p % q
    return p


def egcd(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # return gcd, x, y
    return old_r, old_s, old_t


def modularInv(a, b):
    gcd, x, y = egcd(a, b)

    if x < 0:
        x += b

    return x


def encrypt(e, N, msg):
    cipher = ""

    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, N)) + " "

    return cipher


def decrypt(d, N, cipher):
    msg = ""

    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, N))

    return msg


def main():
    keysize = int(input("Please enter a key size (1024 is default): "))

    print("Hello, This is from Mahdi Hassanzadeh with RSA!")

    e, d, N = generateKeys(keysize)

    msg = "Hello, This is from Mahdi Hassanzadeh with RSA!"

    enc = encrypt(e, N, msg)
    dec = decrypt(d, N, enc)

    print(f"Message: {msg}")
    print(f"e: {e}")
    print(f"d: {d}")
    print(f"N: {N}")
    print(f"enc: {enc}")
    print(f"dec: {dec}")


main()
