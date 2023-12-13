import math

def great_circle_distance(x1,x2,y1,y2):
    radius = 6371.01
    d = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
    return d



def area_of_triangle(x1,y1,x2,y2,x3,y3):
    side1 = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    side2 = math.sqrt(((x3 - x3) ** 2) + ((y3 - y2) ** 2))
    side3 = math.sqrt(((x3 - x1) ** 2) + ((y3 - y1) ** 2))

    s = round((side1 + side2 + side3) / 2)
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    var1 = s - side1
    var2 = s - side2
    var3 = s - side3

    area_1 = s * var1 * var2 * var3
    area = math.sqrt(area_1)
    return area

def area_of_triangle_sides(side1,side2,side3):
    s = round((side1 + side2 + side3) / 2)
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

    var1 = s - side1
    var2 = s - side2
    var3 = s - side3

    area_1 = s * var1 * var2 * var3
    area = math.sqrt(area_1)
    return area

def get_future_day(number_day):
    if number_day == 0:
       return "Sunday"
    elif number_day == 1:
        return "Monday"
    elif number_day == 2:
        return "Tuesday"
    elif number_day == 3:
        return "Wednesday"
    elif number_day == 4:
        return "Thursday"
    elif number_day == 5:
        return "Friday"
    elif number_day == 6:
        return "Saturday"

def isPrimeNumber(number):
    isPrime = True
    for i in range(2, number // 2):
        if number % i == 0:
            isPrime = False
        break

    return isPrime

def isPalindromicNumber(number):

    num_str = str(number)
    reversed_str = num_str[::-1]

    if num_str == reversed_str:
        return True
    else:
        return False


def bubble_sort(l1):
    for j in range(0, len(l1)):
        for i in range(0, len(l1) - 1 - j):
            if l1[i] > l1[i + 1]:
                l1[i], l1[i + 1] = l1[i + 1], l1[i]

    return l1