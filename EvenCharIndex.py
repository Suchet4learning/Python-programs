def main():

    str = input()
    print(str)
    print(type(str))
    print(len(str))

    count = 0

    for i in range(len(str)):
        if i % 2 == 0:
            count+=1
            print(str[i], count, end="|")

    return

if __name__ == '__main__':
    main()