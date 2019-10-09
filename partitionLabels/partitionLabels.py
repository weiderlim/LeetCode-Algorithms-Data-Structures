class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        output = []
        self.S = S

        while len(self.S) > 1:
            self.S_reverse = self.S[::-1]
            first_let_last_ind = len(self.S) - self.S_reverse.index(self.S[0])
            new_last_ind = self.recursion(first_let_last_ind)
            output.append(new_last_ind)
        
        # for the last case where only one letter left
        if len(self.S) == 1:
            output.append(1)

        return output
    
    # have more confidence to use recursion if you think that it applies to the problem
    def recursion (self, last_ind):
        for i in self.S[:last_ind]:
            if i in self.S[last_ind:]:
                new_last_ind = len(self.S) - self.S_reverse.index(i)
                return self.recursion(new_last_ind)
        self.S = self.S[last_ind:]
        return last_ind
        
obj = Solution()
# S = "ababcbacadefegdehijhklij"
S = "qiejxqfnqceocmy"
param = obj.partitionLabels(S)
print (param)

