matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#worst method
a = [[i**2 for i in x if i%2==0] for x in matrix if sum(x) > 7]
print(a)