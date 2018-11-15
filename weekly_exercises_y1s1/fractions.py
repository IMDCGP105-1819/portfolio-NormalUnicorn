class fractions:

    def __init__(self, num, denom, num1, denom1):
        self.num = num
        self.denom = denom
        self.num1 = num1
        self.denom1 = denom1
        self.value1 = float(num/denom)
        self.value2 = float(num1/denom1)

    def addition(self):
        return (self.value1 + self.value2)

    def subtraction(self):
        return (self.value1 - self.value2)

    def division(self):
        return float(self.value1 / self.value2)

    def inverse(self):
        return float(denom/num), float(denom1/num1)

a = fractions(1,2,4,5)
print(a.addition, a.subtraction, a.division, a.inverse)
