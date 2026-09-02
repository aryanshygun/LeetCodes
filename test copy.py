# nums1 = [2,4]
# nums2 = [1,2,3,4]
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]


xdict = {}
stack = []
i = 0
while i < len(nums2):
    while stack and nums2[i] > stack[-1]:
        idx = stack.pop()
        xdict[idx] = nums2[i]
    stack.append(nums2[i])
    i += 1

while stack:
    xdict[stack[-1]] = -1
    stack.pop()

x = [xdict.get(num, 0) for num in nums1]

print(x)
