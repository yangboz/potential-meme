import random
def sample(f):
    x,y = random.random(),random.random()
    return 1 if x*x+y*y <1 else 0
print(sample(30))