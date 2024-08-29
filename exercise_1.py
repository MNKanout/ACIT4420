def main():
    sqr_list = [x**2 for x in range(1,11) if x % 2 == 0]
    print(sqr_list)

    ascii_python = {char: ord(char) for char in 'PYTHON'}
    print(ascii_python)

if __name__ == '__main__':
    main()
