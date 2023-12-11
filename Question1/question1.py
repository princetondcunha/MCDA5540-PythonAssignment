'''Question 1'''

def stack(origlist, operation, new_element=None):
    '''Stack'''
    if operation == 'add':
        if new_element is None:
            print("Nothing to Push")
            return origlist
        origlist.insert(0, new_element)
        return origlist
    elif operation == 'remove':
        if len(origlist) == 0:
            print("Stack is Empty")
            return origlist
        origlist.pop(0)
        return origlist

def queue(origlist, operation, new_element=None):
    '''Queue'''
    if operation == 'add':
        if new_element is None:
            print("Nothing to Enqueue")
        origlist.append(new_element)
        return origlist
    elif operation == 'remove':
        if len(origlist) == 0:
            print("Queue is empty. Nothing to Dequeue")
            return origlist
        origlist.pop(0)
        return origlist

new_list = [1,2,3,4]
print("-----------------------------------------------------------------")
print("Initial List: ", new_list)
print("-----------------------------------------------------------------")

# # Stack - Push
print("Stack - Push: Push 0 to stack")
new_list = stack(new_list,'add',0)
print(new_list)
print("-----------------------------------------------------------------")

# # Stack - Pop
print("Stack - Pop: Pop Top element from the Stack")
new_list = stack(new_list,'remove')
print(new_list)
print("-----------------------------------------------------------------")

# # Queue - Enqueue
print("Queue - Enqueue: Enqueue 5 to Queue")
new_list = queue(new_list,'add',5)
print(new_list)
print("-----------------------------------------------------------------")

# # Queue - Dequeue
print("Queue - Dequeue: Dequeue an element from the Queue")
new_list = queue(new_list,'remove')
print(new_list)
print("-----------------------------------------------------------------")
