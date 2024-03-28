# l1 = [2, 4, 3]
# l2 = [5, 6, 4]
# a = ''.join(map(str, l1[::-1]))
# b = ''.join(map(str, l2[::-1]))
# c = int(a) + int(b)
# xlist = [int(i) for i in str(c)[::-1]]
# print(xlist)


class Solution:
    def addTwoNumbers(self, l1, l2):
        a = ''.join(map(str, l1[::-1]))
        b = ''.join(map(str, l2[::-1]))
        c = int(a) + int(b)
        xlist = [int(i) for i in str(c)[::-1]]
        return xlist  
    
x = Solution()
print(x.addTwoNumbers([2, 4, 3], [5, 6, 4]))