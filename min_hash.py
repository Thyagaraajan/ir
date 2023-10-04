import random

def docToShringle(documents, k):
    shringleSet = []
    
    for key in documents:
        doc = documents[key]
        words = doc.split()
        
        for i in range(len(words) - k + 1):
            shringle = ""
            for j in range(i,i+k):
                word = words[j]
                shringle += word
                if j < i + k -1:
                    shringle += " "
            
            if shringle not in shringleSet:
                shringleSet.append(shringle)
    
    return shringleSet

def getInputDict(shringleSet, documents):
    ch = 65
    inputDict = {}
    
    for shringle in shringleSet:
        tempList = []
        for key in documents:
            doc = documents[key]
            if shringle in doc:
                tempList.append(1)
            else:
                tempList.append(0)
        inputDict[chr(ch)] = tempList
        ch += 1
    
    return inputDict

def minHash(inputDict, shuffle):
    shuffMat = []
    totalDocs = len(inputDict['A'])
    simMat = [[0 for j in range(totalDocs)] for i in range(totalDocs)]
    keyList = list(inputDict.keys())
    
    #find shuffle matrix
    for i in range(shuffle):
        tempList = []
        randKeyList = random.sample(keyList, len(keyList))
        
        for j in range(totalDocs):
            for k in range(len(randKeyList)):
                ch = randKeyList[k]
                if inputDict[ch][j] == 1:
                    tempList.append(k + 1)
                    break;

        shuffMat.append(tempList)
    
    #find similarity matrix
    for i in range(len(simMat)):
        for j in range(len(simMat)):
            if i == j:
                simMat[i][j] = 1
            else:
                count = 0
                for k in range(shuffle):
                    if shuffMat[k][i] == shuffMat[k][j]:
                        count += 1
                simMat[i][j] = count/shuffle
    
    return simMat

def main():    
    documents = {
        "document1":"He moved from London Ontario to London England",
        "document2":"He moved from London England to London Ontario",
        "document3":"He moved from England to London Ontario"
    }
    
    shringleSize = 3
    shringleSet = docToShringle(documents, shringleSize)
    
    inputDict = getInputDict(shringleSet, documents)
    
    shuffles = 3
    simMat = minHash(inputDict, shuffles)
    print(simMat)
    
main()