class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # time complexity --> O(n) for loop here
        grid_max_rows = [max(row) for row in grid]

        # (*grid) unpacks grid before processing the information within. can use for any operator functions if you do not want to unpack using a for loop to go through the list when what you want is a simple operation

        # time complexity --> O(n) for loop here
        grid_max_columns = [max(column) for column in list(zip(*grid))]
        grid_max = []

        # time complexity --> O(n^2) for nested for loops here, although not very big 
        grid_list = [y for x in grid for y in x]

        # time complexity --> O(n^2) for nested for loops here, although not very big 
        for i in grid_max_columns:
            for j in grid_max_rows:
                grid_max.append(min(i,j))

        # time complexity --> O(n) for loop here
        return sum([grid_max[k] - grid_list[k] for k in range(len(grid_max))])

# total time complexity = 3 * O(n) + 2 * O(n^2)

# Runtime: 60 ms, faster than 53.41% of Python online submissions for Max Increase to Keep City Skyline.
# Memory Usage: 12 MB, less than 16.67% of Python online submissions for Max Increase to Keep City Skyline.

obj = Solution()
# grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
grid_2 = [[59,88,44],[3,18,38],[21,26,51]]
param = obj.maxIncreaseKeepingSkyline(grid_2)   

print (param)