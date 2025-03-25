## ###########3Count words in a sentence
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

#############just keep non repeating chars in a string

####approach 1
sentence = "I am a string. I am very useful"
sentence = list(sentence.replace(".",""))
charlist = []
for item in sentence:
  if item not in charlist:
      charlist.append(item)
charlist.remove(" ")
charlist

#### approach 2
sentence = "I am a string. I am very useful"
sentence = set(sentence.replace(".",""))
sentence.remove(" ")
sentence

#find missing digits in range
import random
hi = int(input("Enter highest"))
rng = int(input("Enter a range"))
smallSet = set(random.sample(range(1, hi), rng))
print(smallSet)
fullSet = set(range(1,hi + 1))
print(fullSet)
missing = fullSet.difference(smallSet)
print(missing)
