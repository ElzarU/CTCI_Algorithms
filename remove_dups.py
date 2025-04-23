class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Appends a new node with the given data to the end of the linked list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_dups(self):
        """
        Removes duplicate values from an unsorted linked list.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1) — no additional buffer used.
        
        Logic:
        - For each node (current), we use a runner node to check the rest of the list.
        - If a duplicate is found (runner.next.data == current.data), we skip the node.
        - If not, we move the runner forward.
        - After inner loop, move current forward and repeat.
        
        Example:
        Input: 1 -> 2 -> 3 -> 3 -> 4 -> None
        Output: 1 -> 2 -> 3 -> 4 -> None
        """
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next
        return self.head

    def print_list(self):
        """
        Prints the current state of the linked list.
        Format: val1->val2->...->None
        """
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

# Testing: 
list1 = LinkedList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(3)
list1.append(4)

print("Before removing duplicates:")
list1.print_list()

list1.remove_dups()

print("After removing duplicates:")
list1.print_list()
