'''Write a program that prompts the user to enter the
number of students and each student’s score, and displays the highest and second highest scores'''


number_of_students = eval(input("Enter the number of students: "))


highest_score = 0
second_highest_score = -1


for i in range(number_of_students):
    student_score = eval(input(f"Enter the score for student {i + 1}: "))

    # Update highest and second-highest scores
    if student_score > highest_score:
        second_highest_score = highest_score
        highest_score = student_score
    elif student_score > second_highest_score and student_score != highest_score:
        second_highest_score = student_score

# Check if there is a second-highest score
if second_highest_score == -1:
    print("There is no second-highest score.")
else:
    print(f"The highest score is: {highest_score}")
    print(f"The second-highest score is: {second_highest_score}")