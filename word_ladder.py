import re

# Function for returning how many letters item & target have in common
def same(item, target):
  # Adds the letter c represents to a list if it is in the target as well, number of letters similar is returned
  return len([c for (c, t) in zip(item, target) if c == t])

# Function for returning a list of words one letter different than a certain word
def build(pattern, words, seen, list):
  # Adds 'word' to a list if it is one letter different, not been seen & not in the list already, returns the new list
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]

def find(word, words, seen, target, path):
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  if len(list) == 0:
    return False
  list = sorted([(same(w, target), w) for w in list])
  list = list[::-1]
  for (match, item) in list:
    if match >= len(target) - 1:
      if match == len(target) - 1:
        path.append(item)
      return True
    seen[item] = True
  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()

# Statement for making sure a valid dictionary has been entered
while True:
  try:
    fname = input("Enter dictionary name: ")
    file = open(fname)
    lines = file.readlines()
	
	# Check to see if the dictionary is empty
    if not lines:
      print("The dictionary given is empty")
      continue
    break
  except FileNotFoundError as e:
    print("Dictionary file by that name does not exist. Please try an existing dictionary name.")

# Statement for making sure that valid start and target words have been input
while True:
  start = input("Enter start word:")
  words = []
  for line in lines:
    word = line.rstrip()
    if len(word) == len(start):
      words.append(word)
  if start not in words:
    print("Start word not in dictionary, please try another start word.")
    continue
  target = input("Enter target word:")
  if len(start)!=len(target):
    print("Length of start word and target word is different, please enter 2 words of same length.")
    continue
  if target not in words:
    print("Target word not in dictionary, please try again.")
    continue
  break

count = 0
path = [start]
seen = {start : True}
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")

