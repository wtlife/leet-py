from core.struct import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode()
        pre.next = head
        cur = pre

        while cur.next and cur.next.next:
            start, end = cur.next, cur.next.next
            cur.next = end
            start.next = end.next
            end.next = start
            cur = start

        return pre.next
