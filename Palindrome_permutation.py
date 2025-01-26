def is_permutation_of_palindrome(x):
    # remove spaces and convert strings to lowercase
    x = x.replace(" ", "").lower()

    char_count = {}

    for i in x:
        if i.isalpha():
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1

    odd_count = 0

    for j in char_count.values():
        if j % 2 != 0:
            odd_count += 1

    return odd_count <= 1

a = str(input())
print(is_permutation_of_palindrome(a))


