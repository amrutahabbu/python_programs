def count_consonants_and_vowels(filename):
    vowels = "AEIOUaeiou"
    vowelsSet = set(vowels)
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    consonantsSet = set(consonants)
    vowel_count = 0
    consonant_count = 0

    try:
        with open(filename, 'r') as file:
            text = file.read()

            for char in text:
                if char in vowelsSet:
                    vowel_count += 1
                elif char in consonantsSet:
                    consonant_count += 1

        return vowel_count, consonant_count

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def main():
    filename = input("Enter the filename: ")
    counts = count_consonants_and_vowels(filename)

    if counts:
        vowel_count, consonant_count = counts
        print(f"Vowels: {vowel_count}")
        print(f"Consonants: {consonant_count}")


if __name__ == "__main__":
    main()
