#queue follows FIFO- first in first out
# Basic operations we can do on a queue are:

# Enqueue: Adds a new element to the queue.
# Dequeue: Removes and returns the first (front) element from the queue.
# Peek: Returns the first element in the queue.
# isEmpty: Checks if the queue is empty.
# Size: Finds the number of elements in the queue.

#queue operations
queue = []

while True:
    print("1.Enqueue")
    print("2.dequeue")
    print("3.peek")
    print("4.isEmpty")
    print("5.size")
    print("6.show")
    print("7.exit")

    choice = int(input("Enter your choice:"))
    if choice == 7:
        break

    match choice:
        case 1:
            ele = input("Enter the element to add:")
            queue.append(ele)
            print("Element is added successfully!")
        
        case 2:
            print(f"{queue.pop(0)} is successfully popped!!")
        
        case 3:
            print(f"first element in the queue is {queue[0]}")
        
        case 4:
            if len(queue) == 0:
                print("queue is empty")
            else:
                print(f"Queue is having {len(queue)} elements.")
        
        case 5:
            print(f"the current size of the queue is {len(queue)}")
        
        case 6:
            print(queue)
        
        case _:
            print("Enter the valid choice")

