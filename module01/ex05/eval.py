def valid(coefs, words):
    if not all (isinstance(c, list) for c in [coefs, words]):
        print("ERROR LIST")
        return False
    if not all(isinstance(c, (int, float))  for c in coefs):
        print("ERROR COEF")
        return False 
    if not all(isinstance(c, str) for c in words):
        print("ERROR WORd")
        return False
    if len(coefs) is not len(words):
        print("LEN ERROR")
        return False
    return True

class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if valid(coefs, words) is False:
            return 
        total = 0
       # for i in range(len(words)):
        #    total += len(words[i]) * coefs[i]
       # for i in zip(coefs, words):
       #     total += i[0] * len(i[1])
        for i, word in zip(coefs, words):
            total += i * len(word)
        print(total) 

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if valid(coefs, words) is False:
            return 
        total = 0
        for  i, word in enumerate(words):
            total += len(word) * coefs[i]
        print(total)

if __name__ == "__main__":
    a = Evaluator()
    words = ["Le", "lorem", "Ipsum", "est", "simple"]
    coefs = [1, 4, 1, 4, 0.5]
    a.zip_evaluate(coefs = [1, 2, 1, 4, 0.5] , words=["Le", "lorem", "Ipsum", "est", "simple"])
    a.enumerate_evaluate(coefs = [1, 2, 1, 4, 6, 0.5] , words=["Le", "lorem", "n", "Ipsum", "est", "simple"])

    