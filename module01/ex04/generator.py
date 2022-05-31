import string
def generator(text, sep = " ", option = None):
    if not isinstance(text, str) or not isinstance(sep, str) or option not in ["shuffle", "unique", "ordered"]:
        yield ("ERROR")
        return
    ret = text.split(sep)
    if option == "shuffle":
        ret.sort(key=lambda  x:  2)
    elif option == "ordered":
        ret.sort()
    elif option == "unique":
        ret = [word for i, word in enumerate(ret) if ret[:i].count(word) == 0]
    for word in ret:
        yield word
    return

if __name__ == '__main__':
    text = "Le Lorem Ipsum est du du simplement du faux texte Le ."
    for word in generator(text, sep=" ", option="unique"): 
        print(word)
    for word in generator(text, sep=" ", option="shuffle"): 
        print(word)
    for word in generator(text, sep=" ", option="ordered"): 
        print(word)
    for word in generator(text, sep=" ", option="asdsadsa"): 
        print(word)
