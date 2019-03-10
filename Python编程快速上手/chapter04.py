spam = ["apple", "bananas", "tuft", "cats"]
spam[-1] = "and " + spam[-1]


def listMu(spams):
    str2 = spams[0]
    for i in range(1, len(spams)):
        str2 = str2 + ", " + spams[i]
    return str2


print(listMu(spam))
