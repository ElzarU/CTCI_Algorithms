class Solution:
    def string_compressor(self, MyString):
        """
        Performs basic string compression using the counts of repeated characters.
        If the compressed string is not shorter than the original, returns the original string.

        Parameters:
            MyString (str): The input string containing only lowercase or uppercase letters (a-z, A-Z).

        Returns:
            str: The compressed string if it's shorter, otherwise the original string.

        Logic:
            - Traverse the string from left to right.
            - Count consecutive repeating characters.
            - Append character + count to a result list when a new character is encountered.
            - At the end, compare lengths of original and compressed strings.
              If compressed is not shorter, return the original.
        
        Examples:
            "aabcccccaaa" → "a2b1c5a3" (too long → returns "aabcccccaaa")
            "abc" → "a1b1c1" (returns original because compressed is longer)
        """
        if not MyString: # return " " if string is empty 
            return MyString
        
        compressed = []
        count = 1

        for i in range(1, len(MyString)):
            if MyString[i] == MyString[i-1]:
                count +=1
            else:
                compressed.append(MyString[i-1] + str(count))
                count = 1

        compressed.append(MyString[1] + str(count))
        res = ''.join(compressed)
        return res if len(res) < len(MyString) else MyString

# Testcases:
result = Solution()
print(result.string_compressor("aabcccccaaa"))
print(result.string_compressor("abc"))