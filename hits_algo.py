def findInOutEdges(adjMat):
  edgeDict = {};

  #find incoming and outgoing edges of each node
  for i in range(len(adjMat)):
    incoming = []
    outgoing = []
    for j in range(len(adjMat)):
      if adjMat[i][j] == 1:
        outgoing.append(j)
      if adjMat[j][i] == 1:
        incoming.append(j)
    edgeDict[i] = [incoming, outgoing]

  return edgeDict

def normalizeScore(score):
  totalSum = sum(score)

  for i in range(len(score)):
    score[i] = score[i] / totalSum

  return score

#function to calculate hub & authority score
def calcScore(edgeDict, score, flag):
  newScore = []

  for i in range(len(score)):
    val = 0
    edgeList = edgeDict[i][flag]
    for j in range(len(edgeList)):
      val += score[edgeList[j]]
    newScore.append(val)

  return normalizeScore(newScore)

def checkConverge(authScore, newAuthScore, hubScore, newHubScore):
  for i in range(len(authScore)):
    if abs(authScore[i] - newAuthScore[i]) > 0.01:
      return False
    if abs(hubScore[i] - newHubScore[i]) > 0.01:
      return False

  return True

def main():
  #Input Adjacency Matrix
  adjMat = [
      [0,0,0,1,0,0,0,0],
      [0,0,1,0,1,0,0,0],
      [1,0,0,0,0,0,0,0],
      [0,1,1,0,0,0,0,0],
      [0,1,1,1,0,1,0,0],
      [0,0,1,0,0,0,0,1],
      [1,0,1,0,0,0,0,0],
      [1,0,0,0,0,0,0,0]
  ]

  edgeDict = findInOutEdges(adjMat)

  authScore = []
  hubScore = []
  for i in range(len(adjMat)):
    authScore.append(1)
    hubScore.append(1)
  print("Iteration 0:","\n","Authority Score:",authScore,"\n","Hub Score:",hubScore)

  #run until convergence
  iter = 0
  while(1):
    iter += 1
    newAuthScore = calcScore(edgeDict, hubScore, 0)
    newHubScore = calcScore(edgeDict, authScore, 1)

    if(checkConverge(authScore, newAuthScore, hubScore, newHubScore)):
      break;

    authScore = newAuthScore
    hubScore = newHubScore

    print("\n\nIteration ",iter, " :","\n","Authority Score:",authScore,"\n\n","Hub Score:",hubScore)

main()