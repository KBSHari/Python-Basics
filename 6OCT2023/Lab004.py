user=int(input("Enter your multiplication factor: "))
i=0

def multply():
    global i,user
    i+=1
    if(i<=10):
        print(f"2X{i}={user*i}")
        multply()
multply()