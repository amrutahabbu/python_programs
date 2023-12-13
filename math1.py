'''

(Financial application: calculate tips) Write a program that reads the subtotal and
the gratuity rate and computes the gratuity and total. For example, if the user
enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
as the gratuity and 11.5 as the total. Here is a sample run
Enter the subtotal and a gratuity rate: 15.69 , 15
The gratuity is 2.35 and the total is 18.04

'''

sub_total,gratuity_rate = eval(input("Enter the subtotal and gratuity rate"))

gratuity = ((sub_total * gratuity_rate) / 100)
total = sub_total + gratuity

print("The gratuity is " + str(round(gratuity,2)) + " and the total is "+str(round(total,2)))
