class Evennumbers:
    """ clase que implementa un iterador de todos los numero pares hasta
    un maximo"""

    def __init__ (self,max= None):
        self.max= max
# sirve para crear un iterador en un iterable  y con __iter__ lo retorno a si mismo para volver a hacer el ejercicio
    def __iter__(self):
        self.sum=0
        return self
#hace una funcion y retorna para la siguiente vuelta
    def __next__ (self):
        if not self.max or self.num <= self.max:
            result= self.num
            self.num += 2
            return result
        else:
            raise StopIteration