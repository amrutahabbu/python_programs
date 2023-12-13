def generate_permutations(string):
    if len(string) == 0:
        return ['']

    first_char = string[0]
    rest_of_string = string[1:]

    permutations_of_rest = generate_permutations(rest_of_string)

    all_permutations = []
    for perm in permutations_of_rest:
        for i in range(len(perm) + 1):
            new_perm = perm[:i] + first_char + perm[i:]
            all_permutations.append(new_perm)


    return all_permutations

def main():
    input_string = input("Enter a string: ")
    permutations = generate_permutations(input_string)

    print(f"Permutations of '{input_string}':")
    for perm in permutations:
        print(perm)

if __name__ == "__main__":
    main()
