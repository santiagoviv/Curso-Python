
def name(x):
    def repeater (string ):
        #aseguramos que la función repeater sea un string, de lo contrario es falso
        assert type (string)== str , " solo puedes utilizar letras"
        return string * x
    return repeater


def run ():
    start= name (4)
    print (start("hola"))





if __name__== "__main__":
    run ()