'''

(Health application: compute BMI) Body mass index (BMI) is a measure of health
based on weight. It can be calculated by taking your weight in kilograms and
dividing it by the square of your height in meters. Write a program that prompts
the user to enter a weight in pounds and height in inches and displays the BMI.
Note that one pound is 0.45359237 kilograms and one inch is 0.0254 meters.
Here is a sample run

enter weight in pounds: 95.5
Enter height in inches: 50
BMI is 26.8573

'''

weight_in_pounds = eval(input("Enter the weight in pounds "))
height_in_inches = eval(input("Enter the height in inches "))

wt_in_kg = weight_in_pounds * 0.45359237
ht_in_metres = height_in_inches * 0.0254

BMI = round(wt_in_kg / (ht_in_metres ** 2),4)
print("BMI is " + str(BMI))

