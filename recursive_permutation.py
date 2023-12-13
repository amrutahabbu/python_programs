
def generate_permutations(s, left_index, right_index):
    if left_index == right_index:
        print(''.join(s))
    else:
        for i in range(left_index, right_index + 1):
            # Swap the current character with the first character
            # and recursively generate permutations for the rest of the string.
            s[left_index], s[i] = s[i], s[left_index]
            generate_permutations(s, left_index + 1, right_index)
            # Undo the swap to backtrack and try the next possibility.
            s[left_index], s[i] = s[i], s[left_index]

# Example usage:
input_string = "abcd"
s = list(input_string)
generate_permutations(s, 0, len(s) - 1)