def main():
    number = int(input("Enter a number"));
    sum = 0;

    for i in range(1, number + 1):
        sum += i;
    print(sum);

if __name__ == '__main__':
    main()
    