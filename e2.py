def checkio(s):
    t=0
    q=0
    r=0
    if len(s)>=10:
        print(len(s))
        for x in s:
            p=ord(x)
            if 65<=p<=90:
                t=t+1
            if 97<=p<=122:
                q=q+1
            if 48<=p<=57:
                r=r+1
        if t==0:
            return False
        elif q==0:
            return False
        elif r==0:
            return False
        else:
            return True
    else:
        return False
checkio('A1213pokl')        
checkio('bAse730onE4')
checkio('asasasasasasasaas')
checkio('QWERTYqwerty')
checkio('123456123456')
checkio('QwErTy911poqqqq')
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")