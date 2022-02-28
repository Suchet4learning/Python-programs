def main():

    a,b,c = map(int,input().split())

    if a == b == c:
        print("Equilateral")

    elif a==b or b==c:
        print("isoceles")

    else:
        print("Scalene")

    return 0

if __name__ == '__main__':
    main()