class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid_max_row = []
        grid_max_columns = []
        grid_max_columns_new = []
        grid_max = []

        # time complexity --> O(n) for loop here
        for i in grid:
            grid_max_row.append(max(i))

        # time complexity --> O(n^2) for nested for loops here
        grid_max_columns_new = [y for x in grid for y in x]
    
        # time complexity --> O(n^2) for nested for loops here
        for i in range(len(grid[0])):
            grid_max_columns.append(max([grid_max_columns_new[j] for j in range(i, len(grid_max_columns_new), len(grid[0]))]))
        
        # time complexity --> O(n^2) for nested for loops here
        for j in grid_max_columns:
            for i in grid_max_row:
                grid_max.append(min(i,j))

        # time complexity --> O(n) for loop here
        total_sum = sum([grid_max[i] - grid_max_columns_new[i] for i in range(len(grid_max_columns_new))])

        return total_sum

# total time complexity = 2 * O(n) + 3 * O(n^2)
# Runtime: 56 ms, faster than 76.78% of Python online submissions for Max Increase to Keep City Skyline.
# Memory Usage: 12 MB, less than 16.67% of Python online submissions for Max Increase to Keep City Skyline.

obj = Solution()
# grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
grid_2 = [[59,88,44],[3,18,38],[21,26,51]]
param = obj.maxIncreaseKeepingSkyline(grid_2)   

print (param)