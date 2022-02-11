class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        sum = 0
        for i in range(left,right+1):
            sum = sum + self.nums[i]
        return sum
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

numArray = NumArray([-2, 0, 3, -5, 2, -1]);
print(numArray.sumRange(0, 2)) # return (-2) + 0 + 3 = 1
print(numArray.sumRange(2, 5)) # return 3 + (-5) + 2 + (-1) = -1
print(numArray.sumRange(0, 5)) # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3