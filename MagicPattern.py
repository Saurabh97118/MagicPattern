arr=[int(x) for x in input().split()]  # horizantal inputs in array
y=arr
i=count=0
while i<len(arr):
    arr=y.copy()
    arr.remove(arr[i])
    for j in range(len(arr)-2):
        if(arr[j]<arr[j+2]<arr[j+1]):
            count+=1
            break
    if(count>0):
        print("true")
        break
    elif(count==0 and i==len(arr)-1):
        print("false")
    i+=1



    
    

    
    
    
    


