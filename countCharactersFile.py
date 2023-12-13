def count_characters_words_lines(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
    # Count characters
        character_count = len(text)

        with open(filename, 'r') as file:
            lines = file.readlines()
            # Count characters
        line_count = len(lines)


        # Count words
        words = text.split()
        word_count = len(words)

        print(f"Character count: {character_count}")
        print(f"Word count: {word_count}")
        print(f"Line count: {line_count}")

    except FileNotFoundError:
        print(f'File not found: {filename}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

def main():
    filename = input('Enter the filename: ')
    count_characters_words_lines(filename)

if __name__ == '__main__':
    main()
