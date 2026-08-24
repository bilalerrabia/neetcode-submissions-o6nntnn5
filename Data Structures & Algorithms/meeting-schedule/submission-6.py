"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for h, i in enumerate(intervals):
            for hh, j in enumerate(intervals):
                if h == hh:
                    print(h)
                    continue
                if (i.end < j.end and i.start > j.start) or (j.end < i.end and j.end > i.start) or (i.start == j.start and i.end == j.end):
                    return False
        return True
                