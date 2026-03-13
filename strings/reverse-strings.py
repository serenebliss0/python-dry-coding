def main():
    text = input("Enter a word or sentence\n").strip().lower();
    reversed_text = text[::-1];
    print(f"The text reversed is: \n{reversed_text}\n");

if __name__ == "__main__": main();