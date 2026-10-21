class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x)
        i=0
        while i<len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                merged_item = [intervals[i][0], max(intervals[i][1], intervals[i+1][1])]
            
                intervals[i:i+2]=[merged_item ]
            else:
               i+=1
        return intervals
        