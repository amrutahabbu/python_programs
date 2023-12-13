def sum_digits(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        remaining_digits = n // 10
        return last_digit + sum_digits(remaining_digits)

def main():

        num = int(input("Enter an integer: "))
        result =  sum_digits(num)
        print(f"The sum of the digits in {num} is {result}")


if __name__ == "__main__":
    main()
