# Check for Binary
# https://www.geeksforgeeks.org/problems/check-for-binary/1?page=1&category=Strings&difficulty=School,Basic,Easy&sortBy=difficulty

def isBinary(str):
    #code here
    for i in str:
        if i != "0" and i != "1":
            return False
    return True