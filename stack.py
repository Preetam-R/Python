# A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principl or First-In-Last_Out (FILO)

# Basic operations we can do on a stack are:

# Push: Adds a new element on the stack.
# Pop: Removes and returns the top element from the stack.
# Peek: Returns the top (last) element on the stack.
# isEmpty: Checks if the stack is empty.
# Size: Finds the number of elements in the stack.

# Stacks can be implemented by using arrays or linked lists.


#stack implementation using list

stack = [] #creating a empty stack using list

#push operation
stack.append("a")
stack.append("b")
stack.append("c")

print(stack)

#pop opertaion
if len(stack) == 0:
    print("stack is empty")
else:
    print(f"{stack.pop()} element is poped.")

print(f"stack after pop {stack}")

#peek
print(f"top element od the stack is {stack[-1]}")
#IsEmpty
if len(stack) == 0:
    print("Stack is empty.")

print(f"size of the stack is {len(stack)}")


