import numpy as np

rng = np.random.default_rng(seed = 1)

print(rng.integers(low=1,high=70,size=(3,2)))

# floating point 

print(np.random.uniform(size = (3,2)))

#suffle
rng = np.random.default_rng()

array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

#random choice

fruits = np.array(["apple","orange","banana"])
fruit = rng.choice(fruits)
print(fruit)