# since we can only flip from the front, lets set the values from the back and move to the front. Identify the position of the largest unsorted int and move it to the front before flipping it to the position before the last sorted int.

# Example
# [3, 2, 4, 1] , sort with k = 3
# [4, 2, 3, 1] , sort with k = 4
# [1, 3, 2, 4] , sort with k = 2
# [3, 1, 2, 4] , sort with k = 3
# [2, 1, 3, 4] , sort with k = 2
# [1, 2, 3, 4]


class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        full_len = len(A)
        flip_list = []
        # only need to make changes up to n-1 elements, the final element is the smallest one in the sorted list.
        for i in range(full_len - 1):
            # if the last element is the biggest int just pop the list. A small change is popping the list everytime the biggest value is already sorted, to make the process of looking for max ints easier for each loop.
            if A[-1] != max(A):
                # steps to reverse the front part of the list up to the biggest int.
                if A[0] != max(A):
                    # find position of biggest int given by the variable max_pos.
                    max_pos = A.index(max(A)) + 1
                    # slice and reverse
                    A[:max_pos] = A[:max_pos][::-1]   
                    flip_list.append(max_pos)
                # move the biggest int, which was flipped to the front, now to the back.
                A.reverse()
                flip_list.append(len(A))
                print (A, flip_list)
            A.pop()
            
        return flip_list


obj = Solution()
param_1 = obj.pancakeSort([3, 2, 4, 1])
param_2 = obj.pancakeSort([1, 2, 3, 4])
print (param_1)
print (param_2)

# Runtime: 76 ms, faster than 5.83% of Python online submissions for Pancake Sorting.
# Memory Usage: 11.8 MB, less than 14.29% of Python online submissions for Pancake Sorting.