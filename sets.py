

def remove_duplicates (some_list):
    without_duplicates= []
    for element  in some_list:
        #si no tengo un valor,  le digo al programa que lo ingrese en la lista
        if element not in without_duplicates:
            without_duplicates.append (element)
    return without_duplicates

def run():
    random_list=[1,1,2,2,4]
    print(remove_duplicates(random_list))
    another_way= set(random_list)
    print(list(another_way))
if __name__== "__main__":
    run()