#Your optional code here
#You can import some modules or create additional functions


def checkio(x):
    u=[]
    for y in x:
        if x.count(y)!=1:
            u.append(y)
    return u

list(checkio([1, 2, 3, 1, 3]))
list(checkio([1, 2, 3, 4, 5]))
list(checkio([5, 5, 5, 5, 5]))
list(checkio([10, 9, 10, 10, 9, 8]))
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")