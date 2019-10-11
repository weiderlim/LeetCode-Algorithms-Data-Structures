# strategy is to walk in the direction of 1,1,2,2,3,3,4,4; where 1 is to the east, 1 to the south, 2 to the west, and 2 to the north, and apppend to a list if the the coordinates match the original rectangle. ends when the length of the list equals the size of the original rectangle.

class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        output = [[r0, c0]]
        # walk in direction 1,1,2,2. 
        for i in range(1, 2 * max([R, C]) + 2, 2):
            for j in range(i):
                c0 += 1
                if 0 <= r0 < R and 0 <= c0 < C:
                    output.append([r0, c0])
            for j in range(i):
                r0 += 1
                if 0 <= r0 < R and 0 <= c0 < C:
                    output.append([r0, c0])
            for j in range((i + 1) / 2):
                c0 -= 1
                if 0 <= r0 < R and 0 <= c0 < C:
                    output.append([r0, c0])
                c0 -= 1
                if 0 <= r0 < R and 0 <= c0 < C:
                    output.append([r0, c0])
            for j in range((i + 1) / 2):
                r0 -= 1
                if 0 <= r0 < R and 0 <= c0 < C:
                    output.append([r0, c0])
                r0 -= 1
                if 0 <= r0 < R and 0 <= c0 < C:
                    output.append([r0, c0])

        if len(output) == (R * C):
            return output


obj = Solution()
param_1 = obj.spiralMatrixIII(1, 4, 0, 0)
print (param_1)
param_2 = obj.spiralMatrixIII(5, 6, 1, 4)
print (param_2)


# Runtime: 88 ms, faster than 94.04% of Python online submissions for Spiral Matrix III.
# Memory Usage: 12.9 MB, less than 100.00% of Python online submissions for Spiral Matrix III.