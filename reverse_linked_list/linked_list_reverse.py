class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    #헤드 초기화
    def __init__(self):
        self.head = None
    #         #while 문
    def reverseList(self, head):
        head = [1, 2, 3, 4, 5]
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        print(prev)
        # return prev

print(LinkedList.reverseList(self, head))