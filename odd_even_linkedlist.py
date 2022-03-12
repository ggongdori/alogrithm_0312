# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        # odd = 1st, 3rd..
        odd = head
        # even = 2nd, 4th..
        even = even_head = head.next

        while even:
            odd.next = odd.next.next
            even.next = even.next.next
            even = even.next
            odd = odd.next

        odd.next = even_head
        return head

if __name__ == "__main__":
    s = Solution
    head = [1,2,3,4,5]
    print(s.oddEvenList(head))