"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, peers: List[Interval]) -> bool:
        for i, peer1 in enumerate(peers):
            for j, peer2 in enumerate(peers):
                if i == j:
                    continue
                if peer2.start > peer1.start and peer2.start < peer1.end:
                    return False
                if peer2.end > peer1.end and peer2.start < peer1.start:
                    return False
                if peer2.start == peer1.start:
                    return False

        return True
