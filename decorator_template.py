from datetime import datetime
# este codigo sirve para calcular el tiempo que le toma al codigo en si de ejecutarse

def execution_time(func):
#*args, **kwargs sirven para decirle a la funcion que no importa la cantidad de argumentos posicioneles,
#la funcion la va a recibir al igual de archivos nombrados
    def wrapper (*args, **kwargs):
        initial_time=datetime.now()
        func(*args, **kwargs)
        final_time=datetime.now()
        time_used= initial_time- final_time
        print ("pasaron "+str (time_used.total_seconds()) + "  desde que iniciaste el programa" )
    return wrapper

@execution_time
def random_func ():
    # el _ sirve para que no imprima toda la información en cada vuelta 
    for _ in range (1,1000000):
        pass

@execution_time
def suma (a:int, b: int )->int:
    return a + b

@execution_time
def saludo (nombre= "santiago"):
    print ("hola"+nombre)


random_func()
suma (5,5)
saludo (" mi viejo ")



