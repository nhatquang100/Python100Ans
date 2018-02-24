class Solution:
    def findRestaurant(self, list1, list2):
        d = {}
        result = []
        minimum = (len(list1) + len(list2)-2)
        for i in range(len(list1)):
            d[list1[i]] = i
        for j in range(len(list2)):
            if list2[j] in d:
                index_sum = j + d[list2[j]]
                if index_sum == minimum:
                    result.append(list2[j])
                elif index_sum < minimum:
                    result = [list2[j]]
                    minimum = index_sum
        return result
        