## Count words in a sentence
sentence = "These days code is a necessity. Let's learn to code."
sentence = list(sentence.replace(".","").split())
items = {}

def checkExist(item):
    if item not in items:
        items[item] = 1
    else:
        items[item] = items[item] + 1

list(map(checkExist,sentence))
print(items)
