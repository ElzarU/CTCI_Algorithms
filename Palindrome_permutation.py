class Solution:
    def __init__(self, my_string):
        self.my_string = my_string
        
    #function checks if my_string can be read same forwards and backwards if we rearrange the letters as needed
    def is_permutation_of_palindrome(self):
        self.my_string = self.my_string.replace(" ", "").lower()

        char_count = {}

        for i in self.my_string:
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

#Example usage
my_string = "Tact coa"

result = Solution(my_string)
print(result.is_permutation_of_palindrome())
