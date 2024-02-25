class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ret_list = cur_node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur_node.next = list1
                list1 = list1.next
            else:
                cur_node.next = list2
                list2 = list2.next
            cur_node = cur_node.next
        cur_node.next = list1 or list2
        return ret_list.next