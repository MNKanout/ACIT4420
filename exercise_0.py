def main():

    num = int(input('Enter the number \t'))

    if num == 0:
        return 'The number is zero'

    if num < 0:
        return 'The number is negative'

    if num % 2 == 0:
        return 'The number is positive and even'

    if num % 2 != 0:
        return 'The number is positive and odd'

if __name__ == '__main__':
    print(main())
