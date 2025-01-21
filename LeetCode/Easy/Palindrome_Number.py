class Solution(object):
    def isPalindrome(self, x):
        value = str(x)
        if value[::-1] == str(x):
            return True
        else:
            return False