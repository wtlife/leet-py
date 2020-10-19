from typing import List
from core.struct import ListNode
from core.struct import Node
import collections


class Oct_solution:
    # 24. 两两交换链表中节点
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

    # 1002. 查找常用字符
    def commonChars(self, A: List[str]) -> List[str]:
        ans = []
        minFreq = [float("inf")] * 26
        for word in A:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1

            for i in range(26):
                minFreq[i] = min(minFreq[i], freq[i])

        for i in range(26):
            ans.extend([chr(i + ord("a"))] * minFreq[i])

        return ans

    # 116. 填充每个节点的下一个右侧节点指针
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            for i in range(0, size):
                first = queue.popleft()
                if i < (size - 1):
                    first.next = queue[0]

                if first.left:
                    queue.append(first.left)
                if first.right:
                    queue.append(first.right)

        return root

    # 977. 有序数组的平方
    def sortedSquares(self, A: List[int]) -> List[int]:
        ans = [0] * len(A)
        pos, left, right = len(A) - 1, 0, len(A) - 1
        while pos >= 0:
            if A[left] ** 2 > A[right] ** 2:
                ans[pos] = A[left] ** 2
                left += 1
            else:
                ans[pos] = A[right] ** 2
                right -= 1
            pos -= 1
        return ans

    # 844. 比较含退格的字符串
    def backspaceCompare(self, S: str, T: str) -> bool:
        i, j = len(S) - 1, len(T) - 1
        skipS = skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if S[i] == "#":
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if T[j] == "#":
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if S[i] != T[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1

        return True

    