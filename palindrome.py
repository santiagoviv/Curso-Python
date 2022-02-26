from xmlrpc.client import boolean


# la funcion devuelve un booleano
def is_palindrome (string:str) -> bool:
   #.replace borra espacios y con .lower coloca en minusculas
    string= string.replace (" ", " ").lower()
    return string == string [::-1]

def run ():
    print (is_palindrome("ana"))
     
if __name__== "__main__":
    run ()



