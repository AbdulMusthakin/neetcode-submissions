class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            length = len(seen)
            seen.add(num)
            if len(seen) == length:
                return True
        return False