from matplotlib.dates import num2date


class two_num_calc :
    num1 = 0
    num2 = 0
    def add(self):
        return self.num1 + self.num2
    def sud(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2
    def pow(self):
        return self.num1 ^ self.num2
    def mod(self):
        return self.num1 % self.num2

firstCale = two_num_calc()
firstCale.num1 = 5
firstCale.num2 = 3

secondCale = two_num_calc()
secondCale.num1 = 19564
secondCale.num2 = 47


print("______________firstCale Instance_____________________")
print(firstCale.add())
print(firstCale.sub)
print(firstCale.mul)
print(firstCale.div)
print(firstCale.pow)
print(firstCale.mod())



class Amart :
    price = ""
    수량  = ""
    제품명 = ""
    def report(self):
        print(self.수량)
        print(self.price)

class Bmart :
    price = ""
    수량  = ""
    제품명 = ""
    def report(self):
        print(self.제품명)
        print(self.수량)
        print(self.price)

firstA = Amart()
secondA = Amart()