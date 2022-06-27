mat = list(zip([1,2,3], [3,4,5]))

print(mat)

print(list(map(list, zip(*mat))))