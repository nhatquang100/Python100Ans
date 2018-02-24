class Solution:
    def twoSum(self, numbers, target):
        #list = []
        #for i in range(0,len(numbers)-1):
            #for j in range(i+1 ,len(numbers)):
                #if numbers[i] + numbers[j] == target:
                    #return[i+1,j+1]
        left = 0
        right = len(numbers) -1
        while left < right:
            sum1 = numbers[left] + numbers[right]
            if sum1 < target:
                left +=1
            elif sum1 > target:
                right -=1
            else:
                return left +1, right +1
        return -1,-1