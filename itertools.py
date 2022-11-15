from itertools import product
a = [1,2]
b = [3,4]
pro = product(a,b)
print(list(pro))

c = [1,2]
d = [3]
prod = product(c,d,repeat=2)
print(list(prod))

e = [2,4,6]
f = [1,3,5]
produ = product(e,f)
print(list(produ))

prod1 = product(e,f,repeat = 2)
print(list(prod1))

from itertools  import permutations 
a = [1,2,3]
perm = permutations(a)
print("Permutations=",list(perm))

perm1 = permutations(a,2)
print("Permutations 2 =",list(perm1))

b = [2,4,6]
per = permutations(b)
print("Permutations_own1=",list(per))
per1  = permutations(b,2)
print("Permutations_1=",list(per1))



