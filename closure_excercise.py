def make_division_by (n:int)-> int: 
    def divisor (x:int)-> float:
        assert n !=0, "operación erronea "
        return   x/n 
    return divisor

def run():
  
    example= make_division_by (12)
    print (example(12))

if __name__=="__main__":
    run ()