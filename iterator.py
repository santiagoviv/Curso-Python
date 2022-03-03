class Evennumbers:
    """ clase que implementa un iterador de todos los numero pares hasta
    un maximo"""

    def __init__ (self,max= None):
        self.max= max

    def __iter__(self):
        self.sum=0
        return self

    def __next__ (self):
        if not self.max or self.num <= self.max:
            result= self.num
            self.num += 2
            return result
        else:
            raise StopIteration