class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        second_list_arr = []
        arr_full = []
        deck_sorted = sorted(deck)

        # eliminate single case of n = 1
        if len(deck_sorted) == 1:
            return deck

        # if odd no of elements
        if len(deck_sorted) % 2 != 0:
            first_list = deck_sorted[:int((len(deck_sorted) + 1) / 2)]
            second_list = deck_sorted[int((len(deck_sorted) + 1) / 2):][::-1]
        
        # else even
        else:
            first_list = deck_sorted[:int((len(deck_sorted) / 2))]
            second_list = deck_sorted[int((len(deck_sorted) / 2)):][::-1]

        # dealing with the first use case
        second_list_arr.insert(0,second_list[0])

        for i in range(len(second_list) - 1):
            second_list_arr.insert(0, second_list[i + 1])
            second_list_arr.insert(1, second_list_arr[-1])
            second_list_arr.pop()
        
        # return the last element to the top for a nice arrangement
        if len(deck_sorted) % 2 != 0:
            second_list_arr.insert(0, second_list_arr[-1])
            second_list_arr.pop()

        for i in range(len(first_list)):
            arr_full.append(first_list[i])
            try: 
                arr_full.append(second_list_arr[i])
            except:
                pass
 
        return arr_full

obj = Solution()
param_1 = obj.deckRevealedIncreasing([17,13,11,2,3,5,7,19])
param_2 = obj.deckRevealedIncreasing([1,2,3,4])
print (param_1)
print (param_2)