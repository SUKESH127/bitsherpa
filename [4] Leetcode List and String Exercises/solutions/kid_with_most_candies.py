class Solution:
    # QUESTION: https://leetcode.com/submissions/detail/345906676/
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [c + extraCandies >= max(candies) for c in candies]