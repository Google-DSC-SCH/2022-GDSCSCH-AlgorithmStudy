def solution(phone_book):
    phone_len = set([len(i) for i in phone_book])

    for i in phone_len:
        nolen = [x[:i] for x in phone_book if len(x) != i]
        yeslen = [x[:i] for x in phone_book if len(x) == i]
        print(nolen, yeslen)
        if set(nolen) & set(yeslen):
            return False
    return True
        
