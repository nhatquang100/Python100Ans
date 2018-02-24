class Solution:
    def matrixReshape(self, nums, r, c):
         if r*c != len(nums)*len(nums[0]):
            return nums
         else:
            array = [] 
            for i in range(len(nums)):
                for j in range(len(nums[0])):
                    array.append(nums[i][j])
            #all elements will be added to array

            matrix = []
            while len(array) != 0:
                matrix.append(array[:c])
                array = array[c::]
            return matrix