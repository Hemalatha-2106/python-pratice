def righttriangle(n):
    for i in range(1,n+1):
        print("*"*i)
def lefhttriangle(n):
    for i in range(1,n+1):
        print(""*(n-i)+"*"*i)
def inverserighttriangle(n):
    for i in range(n,0,-1):
        print("*"*i)
def inverselefttriangle(n):
    for i in range(n,0,-1):
        print(""*(n-i)+"*"*i)       
        
               