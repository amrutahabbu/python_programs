def isCCValid(number):
        return (getSize(number) >= 13 and getSize(number) <= 16) and (
                    prefixMatched(number, 4) or prefixMatched(number,5) or prefixMatched(
                number, 37) or prefixMatched(number, 6)) and (
                    (sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)) % 10 == 0)



def sumOfDoubleEvenPlace(number):
        sum = 0
        num = str(number) + ""
        i = getSize(number) - 2
        while (i >= 0):
            sum += getDigit(int(str(num[i]) + "") * 2)
            i -= 2
        return sum



def getDigit(number):
        if (number < 9):
            return number
        return int(number / 10) + number % 10



def sumOfOddPlace(number):
        sum = 0
        num = str(number) + ""
        i = getSize(number) - 1
        while (i >= 0):
            sum += int(str(num[i]) + "")
            i -= 2
        return sum


def prefixMatched(number, d):
        return getPrefix(number, getSize(d)) == d



def getSize(d):
        num = str(d) + ""
        return len(num)



def getPrefix(number, k):
        if (getSize(number) > k):
            num = str(number) + ""
            return int(num[0:k])
        return number


number = int(input("Enter the credit card number for validation"))

print(str(number) + " is " +
          ("valid" if isCCValid(number) else "invalid"))
