import random

# Write your code here!
import math

# Just a suggestion: write a function to calculate the distance to origin.
#
def distance(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

def generate_random_point():
    return [random.random(), random.random()]

def approximate(N=1000):
    # For every point in the range [0, N]
    #   check if it's distance is great than 1
    inside = 0
    for i in range(N):
        point = generate_random_point()
        if distance(*point) <= 1:
            inside += 1

    # Find the ratio of how many are distance<=1
    # and return 4 times that ratio.
    return 4 * (inside / N)

# Try it with a couple N values like 1, 100, 100000,
n = 10
# Since we're using a random number function, the result is different every
# time we run the simulation.
print(approximate(n))
