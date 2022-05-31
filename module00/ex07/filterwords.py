import sys
import string


def ft_split(phrase, size_word): 
    mytable = phrase.maketrans(string.punctuation, ' ' * len(string.punctuation))
    phrase = phrase.translate(mytable)
    print(f"Prev {phrase}")
    phrase = phrase.split(' ')
    new_phrase = []
    for i in phrase:
        if len(i) > size_word:
            new_phrase.append(i)
            #phrase.remove(i)
    res = [word for word in phrase if len(word) > size_word]
    print(f"res = {res}")
    return (new_phrase)

argc = len(sys.argv)
if argc != 3:
    exit("Incorrect argumen")
try:
    s1 = str(sys.argv[1])
    size_word = int(sys.argv[2])
    split_words = ft_split(s1, size_word)
    print(split_words)
except ValueError:
    print("Please insert a string and int")
    exit()
