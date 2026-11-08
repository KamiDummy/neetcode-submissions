class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        dummy_node = ListNode(-1)
        self.head = dummy_node
        self.tail = dummy_node

    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while i <= index and cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        cur = self.head
        i = 0
        while i < index and cur.next:
            cur = cur.next
            i += 1

        if not cur.next:
            return False

        cur.next = cur.next.next
        if cur.next is None:
            self.tail = cur
        return True

    def getValues(self) -> List[int]:
        cur = self.head.next
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next
        return values


