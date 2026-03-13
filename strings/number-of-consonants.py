def main():
    text = input("Enter a word or sentence\n").lower().strip();
    chars = list(text);

    consonant_count = 0;

    for char in chars:
        if char not in "aeiou" and char.isalpha() :
            consonant_count +=1;

    print(chars);
    print(f"You have {consonant_count} consonants");

if __name__ == "__main__": main();