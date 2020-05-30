class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        
        return [baseCandies + extraCandies >= maxCandies for baseCandies in candies]
