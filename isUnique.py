class Solution:
    #initialize variables
    def __init__(self, my_list):
        self.my_list = my_list
    
    # unique() function checks if my_list doesn't contain any duplicates
    def unique(self):
        for i in range(len(self.my_list)):
            for j in range(i+1,len(self.my_list)):
                if self.my_list[i] == self.my_list[j]:
                    return False
        return True

#Example usage
my_list=[1,2,3,4]
result = Solution(my_list)

if result.unique():
    print("List IS unique")
else:
    print("List IS NOT unique")