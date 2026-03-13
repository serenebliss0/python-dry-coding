def main():

    print("When you're done, type `y` to continue");
    numbers = [];
    total = 0;
    while True:
        num = input("Type in multiple numbers, press enter after each value you enter\n");
        
        if num == "y":
            break;

        while True:
            try:
                numbers.append(int(num));
                break;
            except ValueError:
                print("You added invalid values to the array!");
                return

    total = sum(numbers);

    print(f"The sum of elements in the array is: {total}");

if __name__ == "__main__": main()