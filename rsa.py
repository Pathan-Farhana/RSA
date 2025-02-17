import random
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime():
    random.seed()
    while True:
        candidate = random.randint(50, 150)  
        if is_prime(candidate):
            return candidate

def mod_exp(base, exp, mod):
    result = 1
    for _ in range(exp):
        result = (result * base) % mod
    return result

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generate_keypair():
    p = generate_prime()
    q = generate_prime()
    print(f"Generated Primes: p = {p}, q = {q}")
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi and gcd(e, phi) != 1:
        e += 1

    d = 1
    while (d * e) % phi != 1:
        d += 1

    return e, d, n

def encrypt(value, e, n):
    return mod_exp(value, e, n)

def decrypt(value, d, n):
    return mod_exp(value, d, n)


if __name__ == "__main__":
    e, d, n = generate_keypair()
    
    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")


    
    num = int(input("Enter a number to encrypt: "))
    encrypted_num = encrypt(num, e, n)
    decrypted_num = decrypt(encrypted_num, d, n)

    print(f"Original Number: {num}")
    print(f"Encrypted Number: {encrypted_num}")
    print(f"Decrypted Number: {decrypted_num}")

    
    alphabet = input("enter an alphabet: ")
    encrypted_alpha = encrypt(ord(alphabet), e, n)
    decrypted_alpha = decrypt(encrypted_alpha, d, n)

    print(f"Original Alphabet: {alphabet}")
    print(f"Encrypted Alphabet: {encrypted_alpha}")
    print(f"Decrypted Alphabet: {chr(decrypted_alpha)}")
