class A:
    def num1(self):
        num1 = int(1)
        print(num1)
class B(A):
    def num3(self):
        num2 = int(2)
        print(num2)

b1 = B()
b1.num1()
