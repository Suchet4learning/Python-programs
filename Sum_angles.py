def main():

    a,b,c = map(int,input().split())

    if a + b + c == 180:
        print(1)

    else:
        print(0)

    return 0

if __name__ == '__main__':
    main()

