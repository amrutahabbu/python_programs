
input_user = int( input ("Enter an integer, the input ends if it is 0: "))
number_of_positives = 0
number_of_negatives = 0
total = 0
if (input_user!= 0):
   while (input_user != 0):
        if (input_user > 0):
            number_of_positives += 1
        elif (input_user < 0):
            number_of_negatives += 1
        total += input_user
        input_user = int( input ("Enter an integer, the input ends if it is 0: "))
        count = number_of_positives + number_of_negatives
        average = total / count
   print ("The number of positives is", number_of_positives)
   print ("The number of negatives is", number_of_negatives)
   print ("The total is", total)
   print ("The average is", float(average))
else:
  print ("You didn't enter any number.")