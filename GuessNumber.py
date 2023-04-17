import random as r
x=r.randint(0,100)
y=-1
count=0
print("\t \t \t  Start \t \t \t")
while x!=y:
    y=int(input("Enter Number\t"))
    if y>x:
        print("Too High")
    elif x>y:
        print("Too Low")
    
    count=count+1
print(f"Number of Guessing Takes {count}")