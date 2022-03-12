# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def mergeTwoLists(list1, list2):
        head = temp = ListNode(0)
    
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
            # list1.val >= list2.val
            else:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
    
        temp.next = list1 or list2
        return head.next

if __name__ == "__main__":
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]

    print(mergeTwoLists(list1, list2))
