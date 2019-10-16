'''
Created on Feb 18, 2019

@author: dr.aarij
'''
from com.search.node import Node
from com.search.eightPuzzleProblem import EightPuzzleProblem
from com.search.strategy.breadthFirstSearchStrategy import BreadthFirstSearchStrategy

class Search(object):
    '''
    classdocs
    '''


    def __init__(self, searchProblem, searchStrategy):
        '''
        Constructor
        '''
        self.searchProblem = searchProblem
        self.searchStrategy = searchStrategy
        
    def solveProblem(self):
        node = Node(self.searchProblem.initialState(), None, 0, 0, '')
        self.searchStrategy.addNode(node)
        
        duplicateMap = {}
        duplicateMap[node.state.stringRep()] = node.state.stringRep()
        
        result = None
        
        while not  self.searchStrategy.isEmpty():
            currentNode = self.searchStrategy.removeNode()
            
            if self.searchProblem.isGoal(currentNode.state):
                result = currentNode
                break
            
            nextMoves = self.searchProblem.succesorFunction(currentNode.state)
            
            for nextState in nextMoves:
                if nextState.stringRep() not in duplicateMap:
                    newNode = Node(nextState, currentNode, currentNode.depth + 1, currentNode.cost + nextState.cost, nextState.action) 
                    self.searchStrategy.addNode(newNode)
                    duplicateMap[newNode.state.stringRep()] = newNode.state.stringRep()             
        return result
    
    def printResult(self,result):
        if result.parentNode is None:
            print("Game Starts")
            print("Initial State : %s" % result.state.getCurrentState())
            return
        self.printResult(result.parentNode)
        print("Perform the following action %s,  New State is  %s,  cost is %d"%(result.action,result.state.getCurrentState(),result.cost))

if __name__ == "__main__":
#     0,8,7,6,5,4,3,2,1
    goal = [[0,1,2],[3,4,5],[6,7,8]]
    heuristic = MisPlacedTilesEightPuzzleHeuristic(goal)
    searchProblem = EightPuzzleProblem([[0,8,7],[6,5,4],[3,2,1]], goal)
    searchStrategy = BreadthFirstSearchStrategy()
#     searchStrategy = DepthFirstSearchStrategy()
    
   
#     searchStrategy = GreedySearch(heuristic)
    
    search = Search(searchProblem, searchStrategy)
    result = search.solveProblem()
    if result is not None:
        search.printResult(result)
        