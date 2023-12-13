def prefix(str1, str2):

    min_len = min(len(str1), len(str2))
    common_prefix = False
    common_string = ""

    for i in range(min_len):
        if str1[i] == str2[i]:
            common_prefix += True
            common_string = common_string + str1[i]
        else:
            break

    return common_string

def main():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    prefixanswer = prefix(str1, str2)

    if prefixanswer != "":
       print("The common prefix is ",prefixanswer)
    else:
       print("There is no common prefix.")

if __name__ == "__main__":
    main()
