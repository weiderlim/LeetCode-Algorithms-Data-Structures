class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        output = []
        pattern_set = []
        same_unique_let = [i for i in words if len(set(i)) == len(set(pattern))]
        
        for i in pattern:            
            if i not in pattern_set : pattern_set.append(i)

        for i in same_unique_let:
            same_unique_let_set = []

            for j in i:            
                if j not in same_unique_let_set : same_unique_let_set.append(j)

            permutation_pattern = []
            permutation_dict = dict(zip(pattern_set, same_unique_let_set))
    
            for k in pattern:
                permutation_pattern.append(permutation_dict[k])

            if "".join(permutation_pattern) == i:
                output.append(i)  

        return output


obj = Solution()
words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
param = obj.findAndReplacePattern(words, pattern)
print (param)