# Program to remove first n characters from a string.

def main():

    s = input()
    n = int(input())
    s = s[n:]
    print(" The string after removing the first n characters is :",s)
    return

if __name__ == '__main__':
    main()



