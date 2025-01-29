class Solution:
    def __init__(self, str1):
        self.str1 = str1
    
    # function replaces all empty spaces in text with %20
    def URLify(self):
        # replace empty space with %20
        self.str1 = self.str1.replace(" ", "%20")
        return self.str1

# Example Usage

str1 = "Mr John Smith"
result = Solution(str1).URLify()

print(result)