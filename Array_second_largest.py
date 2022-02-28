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

def main():
    print("Enter integer values as Array input: ")
    a = list(map(int,input().split()))
    n = second_largest(a,len(a))
    if n>1:
        print("The second largest element of the array is :",n)
    else:
        print("The array has only one element. ", n)
    return 0
    
if __name__ == '__main__':
    main()



    