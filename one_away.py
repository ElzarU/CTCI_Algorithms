class Solution:
    def one_away(self, str1, str2):
        """
        Determines if two strings are one edit (or zero edits) away.
        An edit can be:
            - inserting one character
            - deleting one character
            - replacing one character

        Parameters:
            str1 (str): The first input string.
            str2 (str): The second input string.

        Returns:
            bool: True if the strings are one edit or zero edits away, False otherwise.

        Case 1: Lengths differ by 1 → only one insert or delete allowed
            Example: "pale" vs "ple" → remove 'a'
            - We compare character by character.
            - On mismatch, we skip one character in the longer string.
            - Each mismatch increments a counter (count += 1).
            - If count exceeds 1, return False.

        Case 2: Lengths are equal → only one replace allowed
            Example: "pale" vs "bale" → replace 'p' with 'b'
            - We compare both strings character by character.
            - On mismatch, increment the counter.
            - If a second mismatch is found, return False.
        """
    
        if abs(len(str1)-len(str2)) > 1:
            return False

        # Ensure s1 is the shorter string
        if len(str1) > len(str2):
            str1, str2 = str2, str1

        i = 0
        j = 0
        count = 0

        while i < len(str1) and j < len(str2):
            if str1[i] != str2[j]:
                count+=1
                if count > 1:
                    return False
                if len(str1) == len(str2): # If lengths are equal, move both pointers (replace)
                    i+=1
            else:
                i+=1 # Characters match, move pointer for shorter string
            j+=1 # Always move pointer for longer string
        return True
    
# Testcases:
result = Solution()
print(result.one_away("pale", "ple"))
print(result.one_away("pales", "pale"))
print(result.one_away("pale", "bale"))
print(result.one_away("pale", "bae"))

