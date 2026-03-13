def main():
    number = int(input("Enter a number\n"));
    product = number
    for i in range(1, number):
        product *= i;

    print(product);

if __name__ == "__main__": main();