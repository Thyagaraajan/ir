import numpy as np

def initaliseMat(size):
    mat = []
   
    for i in range(size):
        tempList = []
        for j in range(size):
            tempList.append(0)
        mat.append(tempList)
   
    return mat

def calcMatrix(adjList, alpha):
    mat = initaliseMat(len(adjList))
   
    for key in adjList:
        tempList = adjList[key]
       
        if len(tempList) == 0:
            for i in range(len(adjList)):
                tempList.append(i+1)
               
        for idx in tempList:
            mat[key][idx] = 1/len(tempList)
               
    for i in range(len(adjList)):
        for j in range(len(adjList)):
            mat[i][j] *= (1-alpha)
            mat[i][j] += (alpha/len(adjList))
   
    return mat

def calcScore(mat, score):
    #prevScore = score

    cnt = 5
    while(cnt):
        finalScore = np.matmul(score, mat)
        score = finalScore
        cnt -= 1
   
    return finalScore

def main():
    alpha = 0.5
   
    #input adjacency list
    adjList = {
        0:[1],
        1:[0,2],
        2:[1]
    }
   
    score = []
    for i in range(len(adjList)):
        score.append(1/len(adjList))
   
    mat = calcMatrix(adjList, alpha)
    finalScore = calcScore(mat, score)
    
    print(finalScore)

main()