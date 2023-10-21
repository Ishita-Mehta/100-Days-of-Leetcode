class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base Cases
        if n == 0:
            return 0 
        if n == 1:
            return 1
        if n == 2:
            return 2
        #initialize an array of size n+1
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        # Now we go from when n = 3 to n (n+1) not included
        for i in range(3, n+1):    
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
