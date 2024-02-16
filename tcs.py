class parent:
    def __init__(self,a):
        self.a=a

    def squre(self):
        print(f'The area of squqre is {self.a*self.a}')
class child(parent):

    def __init__(self,a,b=None):
        super().__init__(a)
        self.b=b

    def  squre(self):
        if self.b is None:
            super().squre()
        else:
            print(f'The area of rectangle is {self.a * self.b}')

obj=child(10,20)
obj.squre()


