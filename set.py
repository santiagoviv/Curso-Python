from ctypes import Union


my_1_set={"heello", "my name  is "," santiago"}
my_2_set={"merhaba","meu nome e", "santiago"}

union= my_1_set - my_2_set
union_2= my_1_set | my_2_set
union_3= my_2_set ^ my_1_set

print (union)
my_2_set.add ("valentina")
print (my_2_set)

