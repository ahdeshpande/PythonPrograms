class Node(object):
    """
    Node class
    """
    def __init__(self, data):
        self.data = data
        self.next = None


def get_length(ll):
    """
    Calculates the length of the linked list

    :param ll: Linked List
    :return: Length of the given list and -1 if circular
    """

    # If list contains only one element
    if ll.next is None:
        return 1

    # Initialize length to 1 as we will start with the 2nd element
    length = 1
    # Start node to check for circular list
    initial_node = ll
    pointer_node = ll.next

    # Keep checking the if there exists a next element or if the next element
    #  is the initial node (in case of circualr list)
    while pointer_node is not None and pointer_node is not initial_node:
        length += 1
        pointer_node = pointer_node.next

    # If pointer node is None (i.e., non-circular list)
    if pointer_node is None:
        return length
    else:
        return -1


def question5(ll, m):
    """
    Function finds the mth element from the end in the given linked list ll

    :param ll: Linked List
    :param m: Element from the end
    :return: Value
    """

    # Check for a valid start node
    if ll is None or type(ll) is not Node:
        return "Enter a valid linked list"

    # Check if m is a valid integer index
    if type(m) is not int:
        return "Enter a valid index"

    # Calculate length of the linked list
    llist_length = get_length(ll)

    # Circular list condition
    if llist_length == -1:
        return "Circular linked list"

    # Check if the given index is less than the length of the linked list
    if m > llist_length:
        return "m should be less than the length of the linked list"

    # Iterate through the list till the mth node from the end
    pointer_node = ll
    for node in range(llist_length - m):
        pointer_node = pointer_node.next

    # Return the data of that mth element from the last
    return pointer_node.data


# Testing
# Create a linked list
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)
node_6 = Node(6)
node_7 = Node(7)
node_6.next = node_7
node_5.next = node_6
node_4.next = node_5
node_3.next = node_4
node_2.next = node_3
node_1.next = node_2

print("\nT1: Invalid list Check")
print("--> " + str(question5(999, 4)))
print("\nT2: Invalid index Check")
print("--> " + str(question5(node_1, 6.4)))
print("\nT3: Invalid index Check")
print("--> " + str(question5(node_1, 9)))
print("\nT4: Valid test case")
print("--> " + str(question5(node_1, 6)))
# Make the list circular
node_7.next = node_1
print("\nT5: Circular linked list test case")
print("--> " + str(question5(node_1, 6)))
