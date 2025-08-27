class Solution:
    def hammingWeight(self, n: int) -> int:
      
        count=0
        while n>0:
            if n%2==0:
                n=n//2
                print(n)

            else:
                count+=1
                # print(count)
                n=n//2    
        return count        