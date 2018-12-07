import sys
import collections
import string as strn
import json

def createDictionary():
    dictionary=[]
    with open('wordList.txt','r') as f:
        for line in f:
            for word in line.split():
               dictionary.append(word)
    return dictionary


def sortedWordList():
    dictionary = createDictionary()
    sortedWordMap = {}
    for word in dictionary:
        key = ''.join(sorted(word))
        if key in sortedWordMap:
            sortedWordMap[key] = sortedWordMap[key]+","+word
        else:
            sortedWordMap[key] = word           
    with open('wordMap.txt', 'w') as f:
        json.dump(sortedWordMap, f)


def getWordMap():
    wordMap = json.load(open('wordMap.txt','r'))
    return wordMap

def constructGraph():
    wordMap = getWordMap()
    graph = {}
    letters = strn.lowercase
    for word in wordMap:
        #remove 1 character
        removeList=[]
        for i in range(len(word)):
            removeWord = ''.join(sorted(word[:i]+word[i+1:])) 
            if( len(removeWord) != 0 and removeWord in wordMap):
                    removeList.append(removeWord)

        #add 1 character
        addList = []
        for char in letters: 
            addWord = ''.join(sorted(word+char))
            if addWord in wordMap:
                addList.append(addWord)
                
        newWordList = removeList + addList
        if newWordList:
            graph[word] = newWordList

    with open('wordTransforms.txt', 'w') as f:
        json.dump(graph, f)
    return graph




if __name__ == '__main__':
    sortedWordList()


