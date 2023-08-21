lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#worst method
a = []
for i in lst:
    a.append(i**2)
print('a:', a)
#worse method
def pow(n):
    return n**2


b = map(pow, lst)
print('b:', list(b))
#better method
c = map(lambda x : x**2, lst)
print('c:', list(c))

#best method
d = [x**2 for x in lst]
print('d:', d)

#list_comprehension and id better tha map and filter!



x = [x**2 for x in lst if x %2==0]
print('x:', x)
 #noisy methof with map and filter

y = map(lambda x : x**2, filter(lambda x: x % 2 == 0, lst))
print('y:', list(y))
# print('y:',list(y))


#same above look for dic or set

dic1 = map(lambda x :(x,  x**2), filter(lambda x: x % 2 == 0, lst))
print('dic1', dict(dic1))

#better method

dict2 = {x : x**2 for x in lst if x %2==0}
print('dic1', dict2)
