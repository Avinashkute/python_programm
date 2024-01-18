from abc import ABC,abstractmethod
class product(ABC):
    def __init__(self,name,price):
        self.name=name
        self.price=price
    @abstractmethod
    def product_detail(self) :
        pass

class Mobile(product):
    def __init__(self,name,price,storage):
        super().__init__(name,price)
        self.storage=storage

    def product_detail(self):
        print(f'{self.name}-{self.price}-{self.storage}')

obj=Mobile('moto',1200,'125GB')
obj.product_detail()