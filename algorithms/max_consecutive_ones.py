class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result, current_max = 0, 0
        
        for num in nums:
            if num == 1:
                current_max += 1
            else:
                if result < current_max:
                    result = current_max
                    
                    if result > len(nums) // 2:
                        return result
                current_max = 0
            
        
        return max(result, current_max)
