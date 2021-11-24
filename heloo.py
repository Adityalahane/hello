class rectangle:
    def __init__(self):
        self.length = length
        self.breadth = breadth
    def area(self):
        self.area = self.length * self.breadth
        return self.area
    def perimeter(self):
        self.perimeter = 2*self.length + self.breadth
        return self.perimeter

if __name__=='__main__':
    length = float(input("enter any number:"))
    breadth = float(input("enter any number :"))
    r = rectangle()
    a = r.area()
    p = r.perimeter()
    print("area of rec is",a)
    print("perimeter of rec is",p)