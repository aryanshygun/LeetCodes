nums = [2,1,5,0,4,6]
nums = [20,100,10,12,5,13]
nums = [1,5,0,4,1,3]
# nums = [1,5,0,4,1,3]
class Solution:
    def increasingTriplet(self, nums) -> bool:
        l, r = 0, 1
        while r < len(nums) - 1:
            if nums[l] < nums[r]:
                # if any(nums[r] < i for i in nums[r+1::]):
                if nums[r] < max(nums[r+1::]):
                    return True
                else:
                    # l = r
                    r += 1
            else:
                l = r
                r += 1
        else:
            return False

x = Solution()
print(x.increasingTriplet(nums))





# if any(i>14 for i in nums[4::]):
#     print('true')
