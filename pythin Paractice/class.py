# d={'cat':'billidibachi','ghora':'ghori','insan':'janwar'}
# print(d.items())
# # nums = [0, 1, 2, 3, 4]
# # squares = [x**2 for x in nums]
# # print(squares)
d = {(x, x + 1): x for x in range(10)}  
print(d.values())