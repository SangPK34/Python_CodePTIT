import math
import sys


class Fraction:
    def __init__(self, num, den):
        g = math.gcd(num, den)
        self.num = num // g
        self.den = den // g

    def __str__(self):
        return f"{self.num}/{self.den}"


a, b = map(int, sys.stdin.read().replace("\ufeff", "").split())
print(Fraction(a, b))

