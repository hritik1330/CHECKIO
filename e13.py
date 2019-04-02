def safe_pawns(sets):
    lst=list(sets)
    x=0
    for i in lst:
        u=ord(i[0])
        p=int(i[1])-1
        s=(chr(u-1)+str(p))
        t=(chr(u+1)+str(p))
        #v=(chr(u)+str(p))
        if s in lst :
            x+=1
        elif t in lst:
            x+=1
        #elif v in lst:
            #x+=1
        else:
            x=x
    return x
    
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")