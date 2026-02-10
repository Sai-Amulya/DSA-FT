from math import sqrt
class Solution:
    def checkprimebrute(self,n):
        if n <= 1:
            return False                # no need of else after this as python exits after something is returned
        count = 0
        i = 1
        while i <= n:
            if n % i == 0: 
                count = count + 1
            i += 1
        return True if count == 2 else False

        
    
    def checkprimeopti(self,n):
        if n <= 1:
            return False
        count = 0
        for i in range(1,int(sqrt(n))+1):
            if n % i == 0:
                count += 1
                if n // i != i:
                    count += 1

        
        return True if count == 2 else False

    
num = int(input())
obj1 = Solution()
print (obj1.checkprimebrute(num))
obj2 = Solution()
print (obj2.checkprimeopti(num))

