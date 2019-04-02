def to_encrypt(s,n):
    t=''
    for x in s:
        if n>0:
            if x.isalpha()==True:
                u=ord(x)
                u=u+n
                if u>122:
                    s=122-ord(x)
                    p=n-s
                    u=97+p-1
                    t+=chr(u)
                else:
                    t+=chr(u)
            else:
                t+=x
        else:
            if x.isalpha()==True:
                    u=ord(x)
                    u=u+n
                    if u<97:
                        m=ord(x)-97
                        o=n+m
                        u=122+o+1
                        t+=chr(u)
                    else:
                        t+=chr(u)
            else:
                t=t+x
    return(t)

        
    

if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")