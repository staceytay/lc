class Solution:
    def jump(self, nums: List[int]) -> int:
        min_steps = 0
        l, r = 0, 0
        while r < len(nums) - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            l, r = r + 1, furthest
            min_steps += 1
        return min_steps
