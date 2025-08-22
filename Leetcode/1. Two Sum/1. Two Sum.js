var twoSum = function(nums, target) {
    let i = 0
    while (i < nums.length) {
        let j = i + 1
        while (j < nums.length) {
            if (nums[i] + nums[j] === target) {
                return [i, j]
            }
            j++
        }
        i++
    }
}



var twoSum = function(nums, target) {
    let xdict = {}
    for (let i = 0; i < nums.length; i++) {
        y = target - nums[i]
        if (y in xdict) return [xdict[y], i]
        xdict[nums[i]] = i
    }
}