from functools import reduce

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(num) for num in str(n)]
        sm = sum(digits)
        product = reduce(lambda x, y: x * y, digits)
        
        return product - sm
