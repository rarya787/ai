total=int(input("Number of bananas in the beginning:  "))
distance=int(input('Distance to cover: '))
cap=int(input('Maximum capacity of camel: '))

lost=0
start=total
for i in range(distance):
    while start>0:
        start=start-cap
        
        if start==1:
            lost=lost-1
        lost=lost+2
    lost=lost-1
    start=total-lost
    if start==0: break
print("left: ",start)
