x = "abc"
z = "123"
try:
    y = int(x)
    print(y)
except:
    y = -1
    print('First', y)


try:
    y = int(z)
    print(y)
except:
    y = -1
    print('Second', y)

# print(int("5"))