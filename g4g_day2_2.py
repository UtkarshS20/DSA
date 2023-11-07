# Check String
# https://www.geeksforgeeks.org/problems/check-string1818/1?page=1&category=Strings&difficulty=School,Basic,Easy&sortBy=difficulty
class Solution:
    def check (self,s):
        # your code here
        # for i in range(len(s)):
        #     if s[i]!=s[i-1]:
        #         return False
        # return True
        s=set(s)
        if len(s)!=1:
            return False
        return True