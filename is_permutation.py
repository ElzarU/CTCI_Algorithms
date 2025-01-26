class Solution:
    # initializing variabless
    def __init__(self, first_string, second_string):
        self.first_string = first_string
        self.second_string = second_string

    #is_permutation function checks is second string is a permutation of the first string
    def is_permutation(self):
        if len(self.first_string) != len(self.second_string):
            return False

        return sorted(first_string)==sorted(second_string)

#Example usage
first_string="qwerty"
second_string = "wertyq"

res = Solution(first_string,second_string)
if res.is_permutation():
    print("second_string IS a permutation of first_string")
else:
    print("second_string IS NOT a permutation of first_string")

