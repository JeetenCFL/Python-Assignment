def stack(our_list, operation, new_element):
    if operation == 'add':
        our_list.append(new_element)
    elif operation == 'remove':
        our_list.pop()
    else:
        print('Invalid operation! There are valid operation: "add" and "remove"')
    
    return our_list


def queue(our_list, operation, new_element):
    if operation == 'add':
        our_list.append(new_element)
    elif operation == 'remove':
        our_list.pop(0)
    else:
        print('Invalid operation! There are valid operation: "add" and "remove"')

    return our_list