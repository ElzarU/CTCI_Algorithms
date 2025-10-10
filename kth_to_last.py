# Implementation of a singly linked list and a method
# to find the kth to last element

class Node:
    """Node class represents a single element in the linked list"""
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    """LinkedList class with basic operations"""
    def __init__(self):
        self.head = None
    
    def append(self, val):
        """Add a new node with value 'val' to the end of the list"""
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def kth_to_last(self, k):
        """
        Return the kth to last node in the linked list.
        Example: For list [1,2,3,4,5] and k=2 → returns node with value 4
        """
        n = 0
        cur = self.head
        # Count total number of nodes
        while cur:
            n += 1
            cur = cur.next
        # Find (n - k)th node from the beginning
        cur = self.head
        for _ in range(n - k):
            cur = cur.next 
        return cur
    
    def print_list(self):
        """Print all values in the linked list"""
        cur = self.head
        while cur:
            print(cur.val, end="->")
            cur = cur.next
        print("None")


# --- Example usage ---
if __name__ == "__main__":
    result = LinkedList()
    result.append(1)
    result.append(2)
    result.append(3)
    result.append(4)
    result.append(5)

    result.print_list()  # Output: 1->2->3->4->5->None

    kth = result.kth_to_last(2)
    print(kth.val)       # Output: 4