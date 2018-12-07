import sys
import collections
import string as strn
import json

def getDictionary():
    dictionary=[]
    with open('wordList.txt','r') as f:
        for line in f:
            for word in line.split():
               dictionary.append(word)
    return dictionary

def getWordMap():
    wordMap = json.load(open('wordMap.txt','r'))
    return wordMap

def getWordTransformGraph():
    wordGraph = json.load(open('wordTransforms.txt','r'))
    return wordGraph
        

def wordLadderSearch():
    
    f=open('output.txt','w')
    if len(sys.argv) != 3:
        f.write("Invalid Input")

    else:
        start = sys.argv[1]
        goal = sys.argv[2]
        dictionary = getDictionary()
        if start not in dictionary or goal not in dictionary:
             f.write("Sorry!!!Either Start or Goal word is not present in dictionary")
        elif start == goal:
            f.write("Start and End Word are same")
        else:
            wordMap = getWordMap()
            graph = json.load(open('wordTransforms.txt','r'))
            sortedStartWord = ''.join(sorted(start))
            sortedEndWord = ''.join(sorted(goal))
            finalPath = []
            paths=collections.deque([[sortedStartWord]])
            extended=set()
            #Breadth First Search
            while len(paths)!=0:
                currentPath=paths.popleft()
                currentWord=currentPath[-1]
                
                if currentWord==sortedEndWord:
                    finalPath = currentPath
                    break
                #already extended this word
                elif currentWord in extended:
                    continue
         
                extended.add(currentWord)
                transforms=graph[currentWord]
                for word in transforms:
                    if word not in currentPath:
                        #avoid loops
                        paths.append(currentPath[:]+[word])
                        
            if not finalPath:
                f.write("")

            else:
                finalPath = finalPath[1:-1]
                f.write(start+'\n')
                for sortedWord in finalPath:
                    f.write(wordMap[sortedWord].split(',')[0]+'\n')
                f.write(goal+'\n')          


if __name__ == '__main__':
    wordLadderSearch()


