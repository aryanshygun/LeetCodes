nums = [2,7,11,15]
target = 9

key = {}
for i in range(len(nums)):
    key[nums[i]] = i
for i in range(len(nums)):
    tmp = target - i
    if tmp in key and key[tmp] != i:
        print(i, key[tmp])