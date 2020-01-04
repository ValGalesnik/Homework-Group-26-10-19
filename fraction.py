#!python3.8.0
# -*-encoding:utf-8-*-


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator != 0:
            self.denominator = denominator
        else:
            raise ZeroDivisionError("Exception! Division by Zero.")

    def __repr__(self):
        self.reduce_fraction()
        return "{numerator}/{denominator}".format(
            numerator=self.numerator,
            denominator=self.denominator)

    def __add__(self, new):
        return Fraction(
            self.numerator * new.denominator + new.numerator * self.denominator,
            self.denominator * new.denominator)

    def __pow__(self, new):
        return Fraction(
            self.numerator ** new.numerator,
            self.denominator ** new.numerator)

    def __sub__(self, new):
        return Fraction(
            self.numerator * new.denominator - new.numerator * self.denominator,
            self.denominator * new.denominator)

    def __truediv__(self, new):
        return Fraction(
            self.numerator * new.denominator,
            self.denominator * new.numerator)

    def __mul__(self, new):
        return Fraction(
            self.numerator * new.numerator,
            self.denominator * new.denominator)

    def reduce_fraction(self):
        for el in range(self.get_greatest(), 0, -1):
            if self.numerator % el == 0 and self.denominator % el == 0:
                self.numerator //= el
                self.denominator //= el

    def get_greatest(self):
        if self.numerator > self.denominator:
            return self.numerator
        return self.denominator


if __name__ == "__main__":
    fraction1 = Fraction(4, 5)
    print(fraction1 + Fraction(1, 8))
    print(Fraction(5, 7) / 10)
    print(Fraction(40, 70))
    print(Fraction(1, 6) + Fraction(1, 3))
    print(Fraction(1, 2) + Fraction(3, 4) + Fraction(1, 9) * Fraction(3, 5))
