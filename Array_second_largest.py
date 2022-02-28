import sys

def second_largest(arr,n):
    ans = None
    # YOUR CODE GOES HERE
    maxValue = -sys.maxsize-1
    nextMax = -sys.maxsize-1

    for i in arr:
        if i>maxValue:
            nextMax = maxValue
            maxValue = i
        else:
            if i>nextMax:
                nextMax=i
    
    if nextMax == -sys.maxsize-1:
        ans = -1
    else:    
        ans = nextMax
        
    return ans

print("Enter integer values as Array input: ")
a = list(map(int,input().split()))
print(second_largest(a,len(a)))




    