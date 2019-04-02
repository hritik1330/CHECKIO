def count_words(text, words):
    s=text.lower()
    y=0
    for x in words:
        if x in s:
            y=y+1
    return y

count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"})
count_words("Bananas, give me bananas!!!", {"banana", "bananas"})
count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",{"sum", "hamlet", "infinity", "anything"})
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")