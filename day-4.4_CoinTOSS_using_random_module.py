# create a virtual coin toss program using random module
import random
test_seed = int(input("create a seed number: "))
random_seed = test_seed
random_side = random.randint(0,1)
if random_side == 0:
    print("Head")
else:
    print("Tail")