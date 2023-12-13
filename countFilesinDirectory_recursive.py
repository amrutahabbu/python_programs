import os


def count_files_in_directory(directory):
    try:
        file_count = 0
        for fileName in os.listdir(directory):
            file_path = os.path.join(directory, fileName)
            if os.path.isfile(file_path):
                file_count += 1
            elif os.path.isdir(file_path):
                # Recursively count files in subdirectories
                file_count += count_files_in_directory(file_path)
        return file_count
    except FileNotFoundError:
        return 0


def main():
    directory = input("Enter a directory path: ")

    if os.path.isdir(directory):
        file_count = count_files_in_directory(directory)
        print(f"Number of files in {directory}: {file_count}")
    else:
        print(f"'{directory}' is not a valid directory.")


if __name__ == "__main__":
    main()
