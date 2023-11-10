# https://www.geeksforgeeks.org/problems/minimum-times-a-has-to-be-repeated-such-that-b-is-a-substring-of-it--170631/1?page=1&sortBy=difficulty
# Minimum times A has to be repeated such that B is a substring of it

class Solution:
    def minRepeats(self, A, B):
        # brute force
        # C=A
        # if B in C:
        #     return 1
        # else:
        #     for i in range(1000):
        #         C+=A
        #         if B in C:
        #             return i+2
        #     return -1
        
        # optimized
        if B in A:
            return 1

        for i in range(1,len(B)//len(A)+3):
            if B in A*i:
                return i
        return -1