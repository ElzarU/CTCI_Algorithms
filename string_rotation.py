class Solution:
    def is_rotation(self, s1, s2):
        """
        Checks if s2 is a rotation of s1 using only one call to isSubstring.

        Parameters:
            s1 (str): The original string.
            s2 (str): The string to check.

        Returns:
            bool: True if s2 is a rotation of s1, False otherwise.

        Logic:
            - Lengths must be equal and non-empty.
            - Concatenate s1 with itself and check if s2 is a substring.
            - hellohello contains elloh(h"elloh"ello) but not "helol". Simply, "helol" is not a part of hellohello
        """
        if len(s1) != len(s2) or not s1:
            return False
        return s2 in (s1 + s1)

# Testcases:
sol = Solution()

print(sol.is_rotation("waterbottle", "erbottlewat"))  # True
print(sol.is_rotation("hello", "lohel"))              # True
print(sol.is_rotation("hello", "elloh"))              # True
print(sol.is_rotation("hello", "helol"))              # False