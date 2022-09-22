def b():
    x = 1
    print('hi')

def a():
    b()


for i in range(3):
    a()
