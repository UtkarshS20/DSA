# Convert a list of characters into a String
# https://www.geeksforgeeks.org/problems/convert-a-list-of-characters-into-a-string5142/1?page=1&category=Strings&difficulty=School,Basic,Easy&sortBy=difficulty
class Solution:
    def chartostr(self, arr,N):
        # code here
        s= ""
        for i in range(N):
            s = s+arr[i]
        return s
