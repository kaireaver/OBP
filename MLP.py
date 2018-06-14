print(list(range(10)))
for n in range(10):
    print(n)
    pass
print("done")

def avg(x,y):
    print("first input is", x)
    print("second input is", y)
    a = (x+y)/ 2
    print("average is", a)
    return a

print(avg(200,301))