#transformar los valores de una lista al cuadrado

def function (x,list):
   
    My_list= []
    for i in list:
        My_list.append(x(i))
    return My_list

def root (n):
    return n**n

print (function(root, [1,2,3,4] ))