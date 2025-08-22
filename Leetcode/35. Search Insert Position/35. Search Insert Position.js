var searchInsert = function(nums, target) {
    if (nums.includes(target)) {
        return nums.indexOf(target)
    }
    let count = 0
    while (count < nums.length) {
        if (nums[count] >= target) {
            break
        }
        count++
    }
    return count

}

let nums = [1,3,5,6]
let target = 2
console.log(searchInsert(nums, target))