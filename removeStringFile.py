def remove_string_from_file(filename, string_to_remove):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        with open(filename, 'w') as file:
            for line in lines:
                modified_line = line.replace(string_to_remove, '')
                file.write(modified_line)

        print(f'Successfully removed "{string_to_remove}" from {filename}.')

    except FileNotFoundError:
        print(f'File not found: {filename}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

def main():
    filename = input('Enter the filename: ')
    string_to_remove = input('Enter the string to remove: ')
    remove_string_from_file(filename, string_to_remove)

if __name__ == '__main__':
    main()
