
def findPrimes(n):
    ar=[]
    for i in range(0,n+1,1):
        ar.append(i)

    ar[0]=0
    ar[1]=0
    i=2
    while True:
        for j in range(i*2,len(ar),i):
            ar[j]=0
            
        for j in range(i+1,len(ar),1):
            if(ar[j]!=0):
                i=j
                break
        else:
            break
    ar.sort()
    ar=ar[ar.index(2):]
    return ar
        
      
ar = findPrimes(100000)

