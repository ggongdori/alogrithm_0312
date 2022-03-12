class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    #헤드 초기화
    def __init__(self):
        self.head = None
    #헤드가 없다면 새 값을 헤드로 지정
    def append(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        node = self.head
        #다음 노드가 있을 때
        while node.next:
            node = node.next
        #마지막 노드
        node.next = Node(data, None)



lst = [1,2,3]
ll = LinkedList()
for e in lst:
    ll.append(e)
print(ll)