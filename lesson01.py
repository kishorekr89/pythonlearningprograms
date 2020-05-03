class Fruit:
    def __init__(self,name,shape):
        self.name=name
        self.shape=shape
    def __repr__(self):
        return f'this is return fumtion'

    def __str__(self):
        return f"This is {self.name} with a shape {self.shape}"

c1=Fruit("Apple","Circle")
repr(c1)
print(c1)
                   