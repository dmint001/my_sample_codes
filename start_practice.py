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

#just keep non repeating chars in a string

sentence = "I am a string. I am very useful"
sentence = list(sentence.replace(".",""))
charlist = []
for item in sentence:
  if item not in charlist:
      charlist.append(item)
charlist.remove(" ")
charlist
