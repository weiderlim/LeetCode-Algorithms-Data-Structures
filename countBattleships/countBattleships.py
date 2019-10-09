# return positions of all the "X", if they are next to each other do not count 

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        pos_list = [[i,j] for i in xrange(len(board)) for j in xrange(len(board[0])) if board[i][j] == "X"]
        print (pos_list)
        if pos_list == []: return 0
        count = 0
        for i in xrange(len(pos_list)):
            if [pos_list[i][0] + 1, pos_list[i][1]] not in pos_list and [pos_list[i][0], pos_list[i][1] + 1] not in pos_list:
                count += 1
        return count

obj = Solution()
param_1 = obj.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]])
print (param_1)
param_2 = obj.countBattleships([[]])
print (param_2)
param_3 = obj.countBattleships([["X",".","X"],["X",".","X"]])
print (param_3)

# Runtime: 972 ms, faster than 6.96% of Python online submissions for Battleships in a Board.
# Memory Usage: 14.8 MB, less than 75.00% of Python online submissions for Battleships in a Board.