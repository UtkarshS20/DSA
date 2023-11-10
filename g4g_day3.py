# https://www.geeksforgeeks.org/problems/find-equal-point-in-string-of-brackets2542/1?page=1&sortBy=difficulty
# Equal point in a string of brackets

class Solution:
    def findIndex(self,str):
        # Your code goes here 
        count = 0
        for i in range(len(str)):
            if str[i]==")":
                count+=1
        return count
