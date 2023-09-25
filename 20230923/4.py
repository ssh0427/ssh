for i in range(0,10):
    for j in range(0,i):
        print("*")
    print()
    
for i in range(0,10):
    for j in range(0,i):
        print("*", end="")
    print()

for i in range(0,10):
    for j in range(0,i):
        print("*", end="a")
    print()



for i in range(0,10):
    for k in range(0,i):
        print(" ", end="")
    for j in range(0,10-i):
        print("*", end="")
    print()



for i in range(0,10):
    for k in range(0,10-i):
        print(" ", end="")
    for j in range(0,i):
        print("*", end="")
    print()



for i in range(0,10):
    for j in range(0,i):
        print("*", end="")
    for k in range(0,10-i):
        print("#", end="")
    print()



for i in range(1,11):
    for j in range(0,10-i):
        print(" ", end="")
    for k in range(0,2*i-1):
        print("*", end="")
    for m in range(0,10-i):
        print(" ", end="")
    print()



