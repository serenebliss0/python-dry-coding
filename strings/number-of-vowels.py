def main():
    text = input("Enter a word or sentence\n").strip();
    chars = list(text);

    vowel_count = 0;

    for char in chars:
        if char in "aeiou" and char.isalpha():
            vowel_count +=1;

    print(chars);
    print(f"You have {vowel_count} vowels");

if __name__ == "__main__": main();