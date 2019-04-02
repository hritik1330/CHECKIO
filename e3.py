def checkio(s):
    x=''.join(e for e in s if e.isalpha())
    p=x.upper()
    #print(p)
    dict={}
    for i in p:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
    #print(dict)
    max=dict[p[0]]
    for x in dict:
        if dict[x]>max:
            max=dict[x]
            c=x
        if max==dict[p[0]]:
            c=p[0]
    #print(c)  
    lst=[]
    for x in dict:
        if dict[x]==max:
            lst.append(x)
    u=lst[0]
    low=ord(u)
    #print(low)
    #print(lst)
    for i in lst:
        if ord(i)<=low:
            low=ord(i)
            w=i.lower()
    return w
   
        
    
      
    
checkio("Hello World!")
checkio("How do you do?")
checkio("One")
checkio("Oops!")
checkio("AAaooo!!!!") 
checkio("abe")

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")