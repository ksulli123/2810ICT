import re
import queue


# Function for returning how many letters item & target have in common
def same(item, target):
    if len(item) != len(target):
        print("words not same length")
        return False
    # Adds chaacter 'c' to a list if it is the same letter as 'f', it then returns the number of common lettes
    return len([c for (c, t) in zip(item, target) if c == t])

# Function for returning a list of words one letter different than a certain word
def build(pattern, words, seen, list):
    if len(pattern) != len(words[0]):
        print("The pattern is invalid for the words in 'words'")
        return False
    # Adds 'word' to a list if it is one letter different, not been seen & not in the list already, returns the list
    return [word for word in words if re.search(pattern, word) and word not in seen.keys() and word not in list]

# Function for getting the guaranteed shortest path
def shortestFind(word, words, target, seen):
    length = len(word)
    wordQueue = queue.Queue()
    wordQueue.put([word], False)

    # Depth First Search using a Queue
    while(not wordQueue.empty()):
        path = wordQueue.get(False)
        word = path[-1]
        list = []
        # Generate all of the words that can be created by changing one letter in node.word
        for i in range(length):
            list += build(word[:i] + "." + word[i + 1:], words, seen, list)

        # Loop through each word in the list
        for w in list:
            seen[w] = True
            # If the word is one away from the target the path has been found
            if same(w, target) == length - 1:
                path.append(w)
                path.append(target)
                return len(path) - 1, path

            # If the word isn't one away from the target place its path in the queue
            new_path = path[::]
            new_path.append(w)
            wordQueue.put(new_path, False)
    return False

# Iterative deepening search to find the words
def IDDFS(start, target, seen, words, path, min, max):
    # Looping from minimum to maximum depth stepping by two
    for limit in range(min, max + 2, 2):
        s = dict(seen)
        if find(start, words, s, target, path, limit):
            return True
    return False

# Recursive depth limited search
def find(word, words, seen, target, path, depth):
    # If the path has reached the maximum depth try a different path
    if len(path) == depth:
        return False
    list = []
    # Looping through each possible character change and getting valid words
    for i in range(len(word)):
        list += build(word[:i] + "." + word[i + 1:], words, seen, list)
    # If there are no words in the list try a different path
    if len(list) == 0:
        return False
    # Sort the words by how similar they are to the target
    list = sorted([(same(w, target), w) for w in list])
    list = list[::-1]
    # If the a full path from the starting word to the target has been found return true
    for (match, item) in list:
        if match >= len(target) - 1:
            if match == len(target) - 1:
              path.append(item)
            return True
        seen[item] = True
    # Call the recursive function again, if it has found the return true
    for (match, item) in list:
        path.append(item)
        if find(item, words, seen, target, path, depth):
            return True
        path.pop()

# Function that returns a list of words from a given dictionary file
def getDict(fname):
    words = []
    try:
        file = open(fname)
        words = file.readlines()
    except FileNotFoundError:
        print("Dictionary file by that name does not exist. Please try an existing dictionary name.")
        return False
    if not words:
        print("The dictionary given is empty")
        return False
    return words

# Function that returns the start & target words if they are valid along with a list of words of the same length
def getInputWords(start, target, wordList):
    words = []
    for line in wordList:
        word = line.rstrip()
        if len(word) == len(start):
            words.append(word)
    if start not in words:
        print("Word is not in the provided dictionary.")
        return False
    if len(start) != len(target):
        print("Length of start word and target word is different, please enter 2 words of same length.")
        return False
    elif target not in words:
        print("Target word not in dictionary, please try again.")
        return False
    elif target == start:
        print("The target and start words cannot be the same, please enter valid words.")
        return False
    return words

# Function that returns a python dictionary, called 'seen', of words not to be used when searching
def getSeenDict(fname, start):
    seen = {start: True}
    try:
        f = open(fname)
        for line in f.readlines():
            word = line.rstrip()
            seen[word] = True
    except FileNotFoundError:
        print("A file by that name could not be found. Try again")
        return False
    if len(seen.keys()) == 1:
        print("Empty file, try again")
        return False
    return seen

# Function for determining what path function to use & then calling the function to get the path, returning the path
def choosePathFunc(start, target, seen, words):
    length = len(start)
    # Asking which function to use
    type = input("Want the shortest path? (y,n): ").lower()
    if type == "y":
        result = shortestFind(start, words, target, seen)
        if result:
            return result
        else:
            print("No Path Exists")
            return False
    elif type == "n":
        path = [start]
        if IDDFS(start, target, seen, words, path, length - same(start, target), length + (length - same(start, target))):
            path.append(target)
            return len(path) - 1, path
        else:
            print("No path found")
            return False
    else:
        print("Incorrect y/n value, please try again.")
        return False


# Using the functions to get the paths
fname = input("Enter dictionary name: ")
wordList = getDict(fname)
if not wordList:
    exit(0)
start = input("Enter start word: ").lower()
target = input("Enter target word: ").lower()
words = getInputWords(start, target, wordList)
if not words:
    exit(0)
chr = input("Eliminate some words? (y/n): ")
if chr == "y":
    fname = input("Enter in a file name: ")
    seen = getSeenDict(fname, start)
    if not seen:
        exit(0)
elif chr == "n":
    seen = {start: True}
else:
    print("Unknown Command")
    exit(0)
result = choosePathFunc(start, target, seen, words)
if result:
    print("Steps:", result[0])
    print("Path:", result[1])
