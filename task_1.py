class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

def display(head):
    current = head
    while current:
        print(f"{current.value} -> ", end="")
        current = current.next
    print("None")

def reverse(head):
    """Reverse the linked list in place and returns the new head."""

    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def merge_two_lists(l1, l2):
    """Merge two sorted linked lists and return the head of the merged list."""
    
    dummy = Node()
    tail = dummy

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    return dummy.next

def get_middle(head):
    """Get the middle node of the linked list."""

    if not head:
        return head
    slow = head
    fast = head
    
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def sort_list(head):
    """Sort the linked list using merge sort and return the new head."""

    if not head or not head.next:
        return head
    
    mid = get_middle(head)
    left = head
    right = mid.next
    mid.next = None

    left = sort_list(left)
    right = sort_list(right)

    return merge_two_lists(left, right)

if __name__ == "__main__":
    # Create a linked list
    l_list = LinkedList()
    l_list.add(4)
    l_list.add(2)
    l_list.add(1)
    l_list.add(3)
    
    print("Original list:")
    display(l_list.head) 

    # Reverse the linked list
    l_list.head = reverse(l_list.head)
    print("Reversed list:")
    display(l_list.head)

    # Sort the linked list
    l_list.head = sort_list(l_list.head)
    print("Sorted list:")
    display(l_list.head)

    # Merge two sorted linked lists
    list_a = LinkedList()
    list_a.add(1)
    list_a.add(3)
    list_a.add(5)

    list_b = LinkedList()
    list_b.add(2)
    list_b.add(4)
    list_b.add(6)

    merged_head = merge_two_lists(list_a.head, list_b.head)
    print("Merged list:")
    display(merged_head)
    