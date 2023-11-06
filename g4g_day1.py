class Solution:
    def longest(self, names, n):
    	# code here
    	max_length = 0
    	for i in range(n):
    	    length = len(names[i])
    	    max_length = max(max_length, length)
    	for i in range(n):
    	    if len(names[i]) == max_length:
    	        return names[i]
    	