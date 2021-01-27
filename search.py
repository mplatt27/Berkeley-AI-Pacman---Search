# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    # nodes will be stored as tuples (coordinate, [path of actions])
    # initialize the initial-state node
    initial_coor = problem.getStartState() 
    initial_node = (initial_coor, [])

    # initialize the frontier using a Stack, put initial-state node in the fronier
    frontier = util.Stack() 
    frontier.push(initial_node)
    
    # initialize the explored disctionary; holds node coordinates as keys, and actions list as value
    explored = {}

    # parents dictionary; holds node coordinates as keys, and node's parent coordinate has value
    # initially had this dictionary to reconstruct path at the end, may no longer be needed
    parents = {}
    parents[initial_coor] = []

    # start loop, run until the frontier is empty

    while (not frontier.isEmpty()): 
        # pop a node from the stack
        curr_coor, curr_action = frontier.pop()

        # add to explored dictionary
        explored[curr_coor] = curr_action

        # check if current node is the goal node; if so return path
        if problem.isGoalState(curr_coor):
            return curr_action

        # for each successor node, append to fronier if not yet explored
        for each in problem.getSuccessors(curr_coor):
            next_coor = each[0]
            next_action = each[1]
            next_node = (next_coor, curr_action + [next_action])
            if next_coor not in explored.keys(): 
                parents[next_coor] = curr_coor
                frontier.push(next_node)
                    


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    # nodes will be stored as tuples (coordinate, [path of actions])
    # initialize the initial-state node
    initial_coor = problem.getStartState() 
    initial_node = (initial_coor, [])

    # initialize the frontier using a Queue, put initial-state node in the fronier
    frontier = util.Queue() 
    frontier.push(initial_node)

    # initialize the explored dictionary; holds node coordinates as keys, and actions list as value
    explored = {}

    # hold parents dictionary; holds node coordinates as keys, and node's parent coordinates as value
    # initially had this dictionary to reconstruct path at the end, may no longer be needed
    parents = {}
    parents[initial_coor] = []

    # start loop, run until the frontier is empty

    while (not frontier.isEmpty()): 
        # pop a node from the queue
        curr_coor, curr_action = frontier.pop()

        # add to explored dictionary
        explored[curr_coor] = curr_action

        # check if current node is the goal node; if so return path
        if problem.isGoalState(curr_coor):
            return curr_action

        # for each successor node, append to fronier if not yet explored
        for each in problem.getSuccessors(curr_coor):
            next_coor = each[0]
            next_action = each[1]
            next_node = (next_coor, curr_action + [next_action])
            if next_coor not in explored.keys(): 
                if next_coor not in parents.keys(): # needs to check parents dict or else expands some nodes again
                    parents[next_coor] = curr_coor
                    frontier.push(next_node)
                    

                

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # nodes will be stored as tuples (coordinate, [actions from parent])
    # initialize the initial-state node
    initial_coor = problem.getStartState() 
    initial_node = (initial_coor, [])

    # initialize the frontier using a PriorityQueue
    # put initial-state node in the fronier with priority 0
    frontier = util.PriorityQueue()
    frontier.push(initial_node, 0)

    # initialize the explored disctionary; holds node coordinates as keys, actions list as value
    explored = {}

    # hold parents dictionary; holds node coordinates as keys, and node's parent coordinates as value
    # initially had this dictionary to reconstruct path at the end, may no longer be needed
    parents = {}
    parents[initial_coor] = []

    # unlike bfs and dfs, we need a cost dictionary for the cost of paths
    # dictionary holds node coordinates as keys, and costs as values
    costs = {}
    costs[initial_coor] = 0
    
    # start loop, run until the frontier is empty

    while (not frontier.isEmpty()): 
        # pop a node from the priority queue
        curr_coor, curr_action = frontier.pop()

        # put in explored dictionary if not already
        if curr_coor not in explored.keys():
            explored[curr_coor] = curr_action

        # check if current node is the goal node; if so return path
        if problem.isGoalState(curr_coor):
            #goal_path = curr_action
            return curr_action

        # for each successor node, calculate new cost and add/update frontier as necessary
        for each in problem.getSuccessors(curr_coor):
            next_coor = each[0]
            next_action = each[1]
            next_cost = problem.getCostOfActions(curr_action) + each[2] # cost of path to node so far + new successor
            next_node = (next_coor, curr_action + [next_action])

            # if the sucessor node is already in the frontier and the new cost is not better than 
            # what we already have, we don't want to change it, else update or add as new
            if next_coor not in explored.keys():
                if next_coor in costs.keys():
                    if costs.get(next_coor) <= next_cost:
                        continue
                parents[next_coor] = curr_coor
                costs[next_coor] = next_cost
                frontier.update(next_node, next_cost) # update will push if not already in frontier 
                


                    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    # nodes will be stored as tuples (coordinate, [actions from parent])
    # initialize the initial-state node
    initial_coor = problem.getStartState() 
    initial_node = (initial_coor, [])

    # initialize the frontier using a PriorityQueue, put initial-state node in the fronier with priority 0
    frontier = util.PriorityQueue()
    frontier.push(initial_node, 0)

    # initialize the explored disctionary; holds node coordinates as keys, and cost as value
    explored = {}

    # hold parents dictionary; holds node coordinates as keys, and node's parent coordinates as value
    # initially had this dictionary to reconstruct path at the end, may no longer be needed
    parents = {}
    parents[initial_coor] = []

    # initialize costs dictinoary to keep track of step-costs (not including heuristics)
    costs = {}
    costs[initial_coor] = 0
    
    # start loop, run until the frontier is empty

    while (not frontier.isEmpty()): 
        # pop a node from the priority queue to expand
        curr_coor, curr_action = frontier.pop()

        # add to explored dictionary
        if curr_coor not in explored.keys():
            explored[curr_coor] = curr_action

        # check if current node is the goal node; if so break out of loop
        if problem.isGoalState(curr_coor):
            #goal_path = curr_action
            return curr_action

        # for each successor node, append to fronier if not yet explored
        for each in problem.getSuccessors(curr_coor):
            next_coor = each[0]
            next_action = each[1]
            next_cost = problem.getCostOfActions(curr_action) + each[2] # update step cost
            next_node = (next_coor, curr_action + [next_action])

            # if the sucessor node is already in the frontier and the new cost + heuristic is not better than 
            # what we already have, we don't want to change it, else update or add as new
            if next_coor not in explored.keys():
                if next_coor in costs.keys():
                    if costs.get(next_coor) <= next_cost:
                        continue
                parents[next_coor] = curr_coor
                costs[next_coor] = next_cost
                frontier.update(next_node, next_cost + heuristic(next_coor, problem)) # will push if not in frontier yet
                




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
