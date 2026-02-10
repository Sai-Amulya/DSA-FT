'''Complexity analysis: O(log₁₀N),The number of iterations in the loop depends on 
the number of digits in the number N. Since each digit is processed once using 
constant time operations (modulo, division, multiplication, and addition), 
the total time taken is proportional to the number of digits, which is log₁₀N. 

Space Complexity: O(1),Only a constant number of variables are used regardless of the size of the input number.'''
class Solution:
    def reverseNumber(self,n):
        revNum = 0
        while n > 0:
            lastdigit = n % 10
            revNum = revNum * 10 + lastdigit
            n = n // 10
        return revNum

num = int(input())
obj = Solution()
print (obj.reverseNumber(num))



    
