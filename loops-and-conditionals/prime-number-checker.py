def main():
    import math;
    number = int(input("Enter a number\n"));

    if number <= 1:
        print("This is not a prime number");
        return

    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            print("This is not a prime number");
            return;

    print("This is a prime number!")

if __name__ == '__main__':
    main()
    