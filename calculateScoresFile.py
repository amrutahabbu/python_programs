# Function to read scores from a file and calculate total and average
def calculate_scores(filename):
    try:

        with open(filename, 'r') as file:
            scores = [float(line.strip()) for line in file]

        total = sum(scores)

        average = total / len(scores)

        print(f"Total Score: {total}")
        print(f"Average Score: {average}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print("Error: The file contains non-numeric data.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


filename = input("Enter the name of the file with scores: ")

calculate_scores(filename)
