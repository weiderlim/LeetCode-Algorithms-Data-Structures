import itertools
import copy

class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        score = []
        row_length = list(range(len(A[0])))
        iter_list = [list(itertools.combinations(row_length,i)) for i in range(1,len(row_length) +1)]
        iter_list_sim = [i for j in iter_list for i in j]

        for i in iter_list_sim:
            # as a general rule, do not pass mutable Python objects (lists, dicts) as arguments, as they will also be modified in the main code base (the original location that calls the function). copy.deepcopy() is a workaround solution if for some reason the structure of code cannot be changed
            deepcopy_A = copy.deepcopy(A)
            new_A = self.change_cols(i,deepcopy_A)
            new_A = self.change_rows(new_A) 
            score.append(self.cal_score(new_A))
        
        return max(score)

    def change_cols(self, col_list, A):
        for i in col_list:
            for j in range(len(A)):
                if A[j][i] == 0: A[j][i] = 1 
                else: A[j][i] = 0
        return A


    def change_rows(self, A):
        new_row_A = []
        for i in A:
            new_row = [1 if x == 0 else 0 for x in i]
            new_row_A.append(i if int("".join(map(str,i))) > int("".join(map(str,new_row))) else new_row)
        return new_row_A

    def cal_score(self,A):
        return sum([int("".join(map(str,i)),2) for i in A])

# strategy is to take every single possible iteration (combinations) of changing the columns and rows, and return the largest sum. 

obj = Solution()
# param_1 = obj.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])
# param_2 = obj.matrixScore([[0,1,1],[1,1,1],[0,1,0]])
# print (param_2)
param_3 = obj.matrixScore([[1,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,1,0,1,1],[1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,1],[1,1,0,0,1,0,0,1,0,0,0,0,1,1,1,1,0,0,0,1],[0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0],[1,1,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,0,0],[0,1,0,0,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,1],[1,1,1,1,0,0,0,0,1,1,1,1,0,1,0,1,1,0,0,1],[0,1,1,0,1,0,0,0,1,1,1,1,1,0,1,0,1,1,1,1],[1,0,0,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,1],[1,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,1,0,0,1],[0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0],[0,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,1,0],[0,0,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0,1,0,0],[1,1,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0],[1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,1,0],[1,1,1,1,1,0,0,0,1,0,0,0,1,1,0,1,0,1,1,0],[0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,1,0,0,0,1],[1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1],[1,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1,0,1,1,0],[1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0]])
print (param_3)

# this solution takes too much time, especially for param_3. Take a different approach where we can check if a particular row or column has more 0's than 1's then flip.

# this solution is part of the brute force solutions, but even the solution on Leetcode says that this solution does not run in the time alloted for bigger inputs. So the idea is correct, just that the execution is a little flawed.

