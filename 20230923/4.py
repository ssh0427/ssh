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



for i in range(1,11,3):
    for j in range(0,10-i):
        print(" ", end="")
    for k in range(0,2*i-1):
        print("*", end="")
    for m in range(0,10-i):
        print(" ", end="")
    print()



# 별 찍기 코드

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/be7b5096-a633-41fc-9d05-7cd03a7b01ad/0f348532-61ca-4a3f-a2eb-aa0094244094/Untitled.png)

```python
for i in range(0,10):
    for j in range(0,i):
        print("*", end="")

    print()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/be7b5096-a633-41fc-9d05-7cd03a7b01ad/89d66ff9-eedb-4b26-b0c2-b89942abd1f5/Untitled.png)

```python
for i in range(0,10):
    for j in range(0,10-i):
        print("*", end="")

    print()
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/be7b5096-a633-41fc-9d05-7cd03a7b01ad/fb1702cb-1980-4589-bb74-11ab63df0030/Untitled.png)

```python
for i in range(0,10):
    for k in range(0,i):
        print(" ", end="")
    for j in range(0,10-i):
            print("*", end="")

    print()
```

end=”” 꼴

```python
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
```

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/be7b5096-a633-41fc-9d05-7cd03a7b01ad/0c233c4e-2031-44bd-870c-666d956b7f0d/Untitled.png)

```python
for i in range(10,0,-1):
    for j in range(0,10-i):
        print(" ", end="")
    for k in range(0,2*i-1):
        print("*", end="")
    for m in range(0,10-i):
        print(" ", end="")
    print()
```

→ for i in range(a,b): 에서는 마지막 b는 포함X 인겨.

즉, 위의 경우에서는 i 값이 10, 9, 8, 7,…,2, 1 까지만 오는겨.

또한, for i in range (a,b): 라면, range(a,b,1) 과 똑같은겨. 1은 굳이 안 쓸 뿐.

ex.

for i in range(1,11,3): 인 경우, 공차가 3인겨.

즉, i=1,4,7,10 만 취해서 요 순서대로 나타나는겨.

```python
for i in range(1,11,3):
    for j in range(0,10-i):
        print(" ", end="")
    for k in range(0,2*i-1):
        print("*", end="")
    for m in range(0,10-i):
        print(" ", end="")
    print()
```

for i in range(1,5):
    for k in range(0,5-i):
        print(" ", end="")
    for j in range(0,i):
        print("*", end="")
    print()




for i in range(0,9):
    for j in range(0,9):
        print(i*j, end=" ")
    print()