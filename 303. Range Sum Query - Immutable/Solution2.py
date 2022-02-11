class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.preSum = [int] * (len(nums) + 1)
        self.preSum[0] = 0
        for i in range(1, len(self.preSum)):
            self.preSum[i] = self.preSum[i - 1] + self.nums[i - 1]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.preSum[right + 1] - self.preSum[left]


numArray = NumArray([-2, 0, 3, -5, 2, -1])
print("result:" + str(numArray.sumRange(0, 2)))  # return (-2) + 0 + 3 = 1
# return 3 + (-5) + 2 + (-1) = -1
print("result:" + str(numArray.sumRange(2, 5)))
# return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
print("result:" + str(numArray.sumRange(0, 5)))
