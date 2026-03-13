def main():
    word = input("Enter a word\n").lower().strip();
    reversed_word = word[::-1]; 
    print(reversed_word);
    if word == reversed_word:
        print("This is a palindrome");
    else:
        print("This is not a palindrome");

if __name__ == "__main__": main();