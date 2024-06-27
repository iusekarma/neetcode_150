# O(n) Space Complexity
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        node = head
        while node:
            if node in s:
                return True
            else:
                s.add(node)
            node = node.next
        return False
    
# The tortoise and hier solution
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False