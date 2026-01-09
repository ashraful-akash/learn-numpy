import numpy as np

array = np.array([
    [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]
])

print(array.ndim)
print(array.shape)
print(array[0][0][0]) #chain indexing
print(array[1,1,1]) #multidimensional indexing

word = array[0,0,0] + array[0,1,1]

print(word)