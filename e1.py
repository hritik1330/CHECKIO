from typing import List, Any


def all_the_same(lst):
    
    if len(lst)==0:
        return True
    else:
        c=lst.count(lst[0])
        if c==len(lst):
            return True
        else:
            return False
all_the_same([1, 1, 1])
all_the_same([1, 2, 1])

all_the_same(['a', 'a', 'a'])
all_the_same([])
all_the_same([1])

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")