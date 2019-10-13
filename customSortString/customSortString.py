class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        output = [j for i in S for j in T if j == i]
        
        for j in T: 
            if j not in S:
                output.append(j)

        return "".join(output)


obj = Solution()
param_1 = obj.customSortString("cba", "abcd")
print param_1

# Runtime: 20 ms, faster than 52.28% of Python online submissions for Custom Sort String.
# Memory Usage: 11.6 MB, less than 66.67% of Python online submissions for Custom Sort String.

# seems like a pretty easy problem for medium level.