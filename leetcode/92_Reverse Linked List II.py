# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def generate_node(arr):

    dummy = ListNode()
    head = dummy
    for curr in arr:
        head.next = ListNode(curr)
        head = head.next
    return dummy.next

def print_node(head):
    list = []
    while head is not None:
        list.append(head.val)
        head = head.next
    print(list)

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left < 1 or right < left:
            return head
        index = 0
        from_node = None
        to_node = None
        curr_node = head
        helper = None
        while curr_node is not None :
            index +=1
            from_node = curr_node if index == left-1 else from_node
            to_node = curr_node if index == right + 1 else to_node
            curr_node = curr_node.next

        curr_node = head if from_node is None else from_node.next
        helper = curr_node.next
        curr_node.next = to_node
        while (helper != to_node):
            temp_node = ListNode()
            temp_node = helper.next
            helper.next = curr_node
            curr_node = helper
            helper = temp_node

        if from_node is not None:
            from_node.next = curr_node
            return head
        return curr_node
if __name__ == "__main__":
    s1 = Solution()
    head1 = generate_node([1, 2, 3, 4, 5, 6])
    res = s1.reverseBetween(head1,3,5)
    print_node(res)

