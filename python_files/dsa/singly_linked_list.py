class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next: Node = None


class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None

    def append(self, data: int) -> None:
        new_node: Node = Node(data)

        if not self.head:
            self.head = new_node
            return

        last: Node = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def prepend(self, data: int) -> None:
        new_node: Node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key: int) -> None:
        prev: Node = None
        current: Node = self.head
        while current:
            if current.data == key:
                pass

            current = current.next

    def display(self) -> None:
        current: Node = self.head

        while current:
            print(current.data, end=" -> ")

            current = current.next

        print("None")


ll: LinkedList = LinkedList()
ll.append(20)
ll.append(30)
ll.append(40)
ll.prepend(10)
ll.display()
