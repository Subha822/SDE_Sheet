class Solution(object):
    def triangleType(self, nums):
       a,b,c = nums 
       if a+b <=c or b+c <= a or c+a <=b:
            return "none"
       elif a==b==c:
            return "equilateral"
       elif a==b or b==c or c==a:
            return "isosceles"
       else:
            return "scalene"
