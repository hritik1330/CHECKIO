from typing import List

def checkio(l):
    l1=list(l[0])
    l2=list(l[1])
    l3=list(l[2])
    lst=[l1,l2,l3]
    for j in range(3):
        
        if lst[j][0]==lst[j][1]==lst[j][2] and lst[j][0]!=".":
            return lst[j][0]
            break
        elif lst[0][j]==lst[1][j]==lst[2][j] and lst[0][j]!=".":
            return lst[0][j]
            break
    if lst[0][0]==lst[1][1]==lst[2][2] and lst[0][0]!=".":
        return lst[0][0]
    elif lst[0][2]==lst[1][1]==lst[2][0] and lst[0][2]!=".":
        return lst[0][2]
    else:
        return "D"
        


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")