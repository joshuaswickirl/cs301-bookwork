def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + \
                    self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    # Multiplication method
    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den* other.den
        common_div = gcd(new_num,new_den)
        return Fraction(new_num//common_div, new_den//common_div)

    # Division method
    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        common_div = gcd(new_num,new_den)
        return Fraction(new_num//common_div, new_den//common_div)

    # Subtraction method
    def __sub__(self, other):
        # get common den
        first_num = self.num * other.den
        second_num = other.num * self.den
        common_den = other.den * self.den
        # subtract nums
        new_num = first_num - second_num
        common_div = gcd(new_num,common_den)
        return Fraction(new_num//common_div, common_den//common_div)

    # Greater than method
    def __gt__(self, other):
        # get common den
        first_num = self.num * other.den
        second_num = other.num * self.den
        common_den = other.den * self.den
        # compare numerators
        if first_num > second_num:
            return True
        else:
            return False

    # Greater than method
    def __lt__(self, other):
        # get common den
        first_num = self.num * other.den
        second_num = other.num * self.den
        common_den = other.den * self.den
        # compare numerators
        if first_num < second_num:
            return True
        else:
            return False

x = Fraction(1,2)
y = Fraction(2,3)
print(x+y)
print(x == y)
print(x * y)
print( x / y)
print(x - y)
print(x > y)
print(x < y)