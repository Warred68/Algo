a = 0
b = 10

while b != 0:
    a += 1
    b -= 1
    while a < b: 
        print('a=', a)
        break
    if b%2 != 0:
        print('b=', b)