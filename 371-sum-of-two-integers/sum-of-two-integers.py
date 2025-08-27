class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xFFFFFFFF
        Max_int=0x7FFFFFFF
        while b!=0:
            carry=(a&b)<<1
            a=(a^b )&mask
            b=(carry)&mask
       
        return a if a<Max_int else ~(a ^ mask)

# class Solution:
#     def getSum(self, a: int, b: int) -> int:
#         # 32-bit mask in hexadecimal
#         MASK = 0xFFFFFFFF
#         MAX_INT = 0x7FFFFFFF
        
#         while b != 0:
#             # ^ -> XOR (sum without carry)
#             # & -> AND (common bits), <<1 -> carry
#             carry = (a & b) << 1
#             a = (a ^ b) & MASK  # apply mask to keep it 32-bit
#             b = carry & MASK
        
#         # If a is greater than MAX_INT, it means it's negative in 32-bit signed representation
#         return a if a <= MAX_INT else ~(a ^ MASK)
