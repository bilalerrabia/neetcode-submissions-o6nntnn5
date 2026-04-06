# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headsave = head
        savelist = []
        while head:
            savelist.append(head.val)
            head = head.next
            # print(savelist)
        head = headsave
        i = 0
        Len = len(savelist)
        savelist.reverse()
        # print(head)
        # print(Len)
        # savelist.reverse()
        while i < Len:
            tmp = savelist.pop(0)
            # print(tmp)
            head.val = tmp
            head = head.next
            i += 1
            # print(head.val)
        return headsave
