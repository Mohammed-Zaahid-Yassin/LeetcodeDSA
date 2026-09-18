class Solution:
    def isPalindrome(self, x: int) -> bool:
        value=0
        remainder=x
        if x<0:
            return False

        while remainder!=0:
            value=value*10+(remainder%10)
            remainder//=10
        if value==x:
            return True
        else:
            return False 
