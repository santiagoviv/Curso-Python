import time
class fibbonacci ():
  
    def __init__ (self, max):
        self.max= max
        pass
    def __iter__(self):
        self.n1=0
        self.n2=1
        self.counter=0
        return self
        
    def __next__(self ):
    

        if self.counter==0:
            self.counter +=1
            return self.n1
        elif self.counter ==1:
            self.counter +=1
            return self.n2
       
        else:
           if self.counter  <=self.max:
               self.aux= self.n1+self.n2
               self.n1=self.n2
               self.n2= self.aux
               self.counter +=1
               return self.aux


if __name__== "__main__":
    #con esto guardo el iterador llamado fibonacci
    Fibonacci =fibbonacci ()
    for element in Fibonacci:
        print (element)
        #con este metodo, paramos el tiempo 0,05 segundos para saber que esta haciendo el iterador 
        time.sleep (1)
