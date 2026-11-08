class ListNode:

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        i = 0
        cur = self.head.next
        while cur:
            if i == index:
                return cur.value
            i += 1
            cur = cur.next
        return -1

    def insertHead(self, val: int) -> None:
        node = ListNode(val, self.head.next)
        self.head.next = node
        if not node.next:
            self.tail = node

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        self.tail.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while i < index and cur:
            cur = cur.next
            i += 1
        
        if cur and cur.next: 
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        result = []
        cur = self.head.next
        while cur:
            result.append(cur.value)
            cur = cur.next
        return result
    


linked_list = LinkedList()
linked_list.insertHead(2)
linked_list.insertTail(3)
print(linked_list.remove(1))
