"""
In search.py, you will implement generic search algorithms
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def is_goal_state(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def DFS_rec_func(problem: SearchProblem, state, action, visited):
    if problem.is_goal_state(state):
        return [action]
    visited[state] = True
    for successor, _action, _ in problem.get_successors(state):
        if visited.get(successor) is None:
            result = DFS_rec_func(problem, successor, _action, visited)
            if result is not None:
                return [action] + result
    return None


def depth_first_search(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    ls = DFS_rec_func(problem, problem.get_start_state(), None, {})
    return ls[1:]


def breadth_first_search(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # BFS Algorithm using a queue
    Q = util.Queue()
    visited = {}
    Q.push(problem.get_start_state())
    visited[problem.get_start_state()] = (None, None)
    endPoint = None
    while not Q.isEmpty():
        state = Q.pop()
        if problem.is_goal_state(state):
            endPoint = state
            break
        for successor, action, _ in problem.get_successors(state):
            if visited.get(successor) is None:
                visited[successor] = (state, action)
                Q.push(successor)

    # Reconstruct the path
    action_queue = util.Queue()
    while endPoint is not None:
        state, action = visited[endPoint]
        if action is not None:
            action_queue.push(action)
        endPoint = state
    return action_queue.list


def uniform_cost_search(problem):
    """
    Search the node of least total cost first.
    """
    fitst_state = problem.get_start_state()
    fitst_state.__class__.__lt__ = lambda x, y: (True)
    problem.get_successors(fitst_state)[
        0][1].__class__.__lt__ = lambda x, y: (True)
    visited = {}
    tail = None
    fringe = util.PriorityQueue()
    fringe.push((problem.get_start_state(), None, None, 0), 0)
    while not fringe.isEmpty():
        state, father, action, cost = fringe.pop()
        if problem.is_goal_state(state):
            tail = state
            visited[state] = (father, action)
            break
        if visited.get(state) is None:
            visited[state] = (father, action)
            for successor, saction, stepCost in problem.get_successors(state):
                stepCost = problem.get_cost_of_actions([saction])
                if visited.get(successor) is None:
                    fringe.push((successor, state, saction,
                                cost + stepCost), cost + stepCost)
    actions = util.Queue()
    while tail is not None:
        father, action = visited[tail]
        if action is not None:
            actions.push(action)
        tail = father
    return actions.list


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    open_set = util.PriorityQueue()
    inOpenSet = {}
    cameFrom = {}

    gScore = {}
    gScore[problem.get_start_state()] = 0

    fScore = {}
    fScore[problem.get_start_state()] = heuristic(
        problem.get_start_state(), problem)

    open_set.push(problem.get_start_state(), fScore[problem.get_start_state()])
    inOpenSet[problem.get_start_state()] = True
    while not open_set.isEmpty():
        current = open_set.pop()
        inOpenSet[current] = None
        if problem.is_goal_state(current):
            total_path = util.Queue()
            p = current
            while cameFrom.get(p) is not None:
                current, action = cameFrom[current]
                total_path.push(action)
                p = current
            return total_path.list
        for successor, action, stepCost in problem.get_successors(current):
            tentative_gScore = gScore[current] + stepCost
            if tentative_gScore < gScore.get(successor, float('inf')):
                cameFrom[successor] = (current, action)
                gScore[successor] = tentative_gScore
                fScore[successor] = gScore[successor] + \
                    heuristic(successor, problem)
                if inOpenSet.get(successor) is None:
                    open_set.push(successor, fScore[successor])
    return []


# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
