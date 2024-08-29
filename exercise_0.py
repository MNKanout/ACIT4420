def main():
    num = int(input('Enter the number \t'))

    if num == 0:
        return 'The number is zero'

    elif num > 0:
        if num % 2 == 0:
            return 'The number is positive and even'

        else:
            return 'The number is positive and odd'
    elif num < 0:
        return 'THe number is negative'

if __name__ == '__main__':
    print(main())
