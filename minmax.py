import sys
maxSize = sys.maxsize
print(maxSize)
minSize = -sys.maxsize - 1
print(minSize)

def maxofnum(a,b,c):
    
    ans = None

    if (a>b) and (a>c):
        ans = a
    elif b>c:
        ans = b
    else:
        ans = c

    return ans

def main():

    a = input("Enter the first value: ")
    b = input("Enter the second value: ")
    c = input("Enter the final value: ")

    a = int(a)
    b = int(b)
    c = int(c)

    maxval = maxofnum(a,b,c)
    print("The largest of the 3 numbers is :", maxval)

    return

if __name__ == '__main__':
    main()