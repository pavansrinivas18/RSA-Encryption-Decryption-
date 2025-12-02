# rsa_algorithm.py
# RSA Algorithm Implementation (Key Generation, Encryption, Decryption)

from sympy import randprime, mod_inverse
import random
from utils import gcd

class RSA:
    def __init__(self):
        self.public_key = None
        self.private_key = None

    def generate_keys(self):
        """Generate public and private RSA keys"""
        print("🔑 Generating RSA keys...")

        # Step 1: Choose two random primes
        p = randprime(100, 500)
        q = randprime(100, 500)
        n = p * q
        phi = (p - 1) * (q - 1)

        # Step 2: Choose e (public exponent)
        e = random.randrange(2, phi)
        while gcd(e, phi) != 1:
            e = random.randrange(2, phi)

        # Step 3: Compute d (private exponent)
        d = mod_inverse(e, phi)

        # Step 4: Set public and private keys
        self.public_key = (e, n)
        self.private_key = (d, n)

        print(f"✅ Generated primes: p={p}, q={q}")
        print(f"✅ Public Key: (e={e}, n={n})")
        print(f"✅ Private Key: (d={d}, n={n})")

    def encrypt(self, message: str) -> list:
        """Encrypt message using the public key"""
        e, n = self.public_key
        cipher = [(ord(char) ** e) % n for char in message]
        return cipher

    def decrypt(self, cipher: list) -> str:
        """Decrypt cipher using the private key"""
        d, n = self.private_key
        plain = ''.join([chr((char ** d) % n) for char in cipher])
        return plain
