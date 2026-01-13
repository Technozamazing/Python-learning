# Here working with the random:

# We will first create a obj(rng) to access its methods

# Its methods are:
# rng.integers
# rng.shuffle(array)
# rng.choice(array)



import numpy as np

# # For random number generator
# # rng = np.random.default_rng()
# rng = np.random.default_rng(seed=1)
# # print(rng.integers(1, 7, (2,3)))
# print(rng.integers(low=1, high=10, size=(3, 3)))

# # Concept of seed:
# # seed preserves or stores outcomes of an event
# # so that when we want to get that same result later on we can recall it by using that seed.




# # # For floating point random number:
# np.random.seed(seed=1)     # We cannot pass-on seed value through uniform as in default_rng, so we reseed directly.
# rng = np.random.uniform(low=-8, high=12, size=(3, 2))     # --> returns floting point value from a uniform distribution. By default it returns values from 0 to 1.
# print(rng)



# For Shuffleing in an Array:
rng = np.random.default_rng()
arr = np.array([1, 2, 3, 4, 5])
rng.shuffle(arr)
print(arr)



# For choice:
arr = np.array([['🍇', '🍈', '🍉'], 
                ['🍊', '🍏', '🍎'], 
                ['🍍', '🍌', '🍐']])
fruit = rng.choice(arr, size=(2, 2))
print(fruit)