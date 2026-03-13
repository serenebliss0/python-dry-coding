def main():
    import math;

    count = 0;
    number = 2;
    prime_numbers = [];

    while count < 100:
        is_prime = True;

        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                is_prime = False;
                break

        if is_prime:
            prime_numbers.append(number);
            print(f"{number} is a prime number");
            count += 1;

        number+=1;

if __name__ == '__main__':
    main()
    