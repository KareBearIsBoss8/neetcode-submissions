class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        
        def helper (amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            
            ans = float('inf')
            
            for i in coins:
                if amount - i >= 0:
                    ans = min(ans, 1 + helper(amount - i))
            
            dp[amount] = ans
            return ans
        
        change = helper(amount)
        
        if change >= float('inf'):
            return -1
        
        return change
