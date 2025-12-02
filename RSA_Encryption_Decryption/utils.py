# utils.py
# Utility functions for mathematical operations in RSA

def gcd(a, b):
    """Compute the Greatest Common Divisor using Euclid's Algorithm"""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """Compute modular inverse of e under modulo phi"""
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return None
