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