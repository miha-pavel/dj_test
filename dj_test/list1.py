lst = [1, 2, 3, 4, 5, 6]
lst2 = [i**2 for i in lst if i > 3]
lst3 = {i:i**2 for i in lst if i > 3}
print('lst3: ', lst3)
