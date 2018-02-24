class Solution:
    def constructRectangle(self, area):
        w = int(math.sqrt(area))
        while w >0:
            if area % w == 0:
                return [int(area/w), int(w)]
            w-=1
        