def count_words_address(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()


        # Count words
        words = text.split()
        word_count = len(words)


        print(f"Word count in address: {word_count}")

    except FileNotFoundError:
        print(f'File not found: {filename}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

def main():
    filename = "gettysburg_address"
    count_words_address(filename)

if __name__ == '__main__':
    main()

# Note , I was not able to open the link given in the question. hence I have just counted the number of words.