'''
Suppose that the tuition for a university is $10,000 this year and increases 5% every year. Write a program that
computes the tuition in ten years and the total cost of four years’ worth of tuition
starting ten years from now
'''


tuition_current_year = 10000
tuition_increase_yearly =0.05
total_tuition_tenyears=0
total_tuition_future =0
year=0
while (year<15):
    year=year+1
    tuition_current_year=tuition_current_year*1.05

    if (year==10):
        total_tuition_tenyears=tuition_current_year
print("Tuition in ten years is ",total_tuition_tenyears)

for year in range(10,14,1):
    tuition+=tuition

print("The four-year total tuition in ten years is ",tuition)