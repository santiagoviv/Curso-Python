
def prime_number (prime:int)-> bool:
    operation = [i for i in range (1,prime) if prime % i ==0]
    return len(operation)==0

def run():
    
    print (prime_number(2))


if __name__== "__main__":
    run ()