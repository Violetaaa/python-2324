#!/usr/bin/env python3

class Rational(object):
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def __add__(self, rational):
        return Rational(self.num * rational.den + self.den * rational.num, self.den * rational.den)

    def __sub__(self, rational):
        return Rational(self.num * rational.den - self.den * rational.num, self.den * rational.den)

    def __mul__(self, rational):
        return Rational(self.num * rational.num, self.den * rational.den)

    def __truediv__(self, rational):
        return Rational(self.num * rational.den, self.den * rational.num)

    def __lt__(self, rational):
        return self.num * rational.den < self.den * rational.num
    
    def __gt__(self, rational):
        return self.num * rational.den > self.den * rational.num
    
    def __eq__(self, rational):
        return self.num * rational.den == self.den * rational.num
    
    def __str__(self):
        return f'{self.num}/{self.den}'

    pass

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
