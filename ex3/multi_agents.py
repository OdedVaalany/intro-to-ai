import numpy as np
import abc
import util
from game import Agent, Action
from math import exp


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def get_action(self, game_state):
        """
        You do not need to change this method, but you're welcome to.

        get_action chooses among the best options according to the evaluation function.

        get_action takes a game_state and returns some Action.X for some X in the set {UP, DOWN, LEFT, RIGHT, STOP}
        """

        # Collect legal moves and successor states
        legal_moves = game_state.get_agent_legal_actions()

        # Choose one of the best actions
        scores = [self.evaluation_function(
            game_state, action) for action in legal_moves]
        best_score = max(scores)
        best_indices = [index for index in range(
            len(scores)) if scores[index] == best_score]
        # Pick randomly among the best
        chosen_index = np.random.choice(best_indices)

        "Add more of your code here if you want to"

        return legal_moves[chosen_index]

    def evaluation_function(self, current_game_state, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (GameState.py) and returns a number, where higher numbers are better.

        """

        # Useful information you can extract from a GameState (game_state.py)

        successor_game_state = current_game_state.generate_successor(
            action=action)
        board = successor_game_state.board
        max_tile = successor_game_state.max_tile
        max_tile_current = current_game_state.max_tile
        score = successor_game_state.score
        score_currnet = current_game_state.score
        nempty_current = len(
            current_game_state.get_empty_tiles())
        nempty_succenssor = len(successor_game_state.get_empty_tiles())
        max_score = 0
        for next_action in successor_game_state.get_agent_legal_actions():
            temp_state = successor_game_state.generate_successor(
                action=next_action)
            if temp_state.score > max_score:
                max_score = temp_state.score
        return max_score
        # return (score - socre_currnet) + max_tile - max_tile_current + (nempty_succenssor - nempty_current)*10
        # if max_tile != max_tile_current:
        #     return max_tile
        # return (score - socre_currnet)
        # + 4**(num_of_empty_tiles_successor*(max_tile > 32))
        # if (nempty_current > nempty_succenssor or (max_tile < 8)):
        #     if action in [Action.RIGHT, Action.DOWN]:
        #         return float('inf')
        #     else:
        #         return 0
        # return score

        if (score - score_currnet) < 16:
            return nempty_succenssor
        return score


def score_evaluation_function(current_game_state):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return current_game_state.score


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinmaxAgent, AlphaBetaAgent & ExpectimaxAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evaluation_function='scoreEvaluationFunction', depth=2):
        self.evaluation_function = util.lookup(evaluation_function, globals())
        self.depth = depth

    @ abc.abstractmethod
    def get_action(self, game_state):
        return


class MinmaxAgent(MultiAgentSearchAgent):
    def get_action(self, game_state):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        game_state.get_legal_actions(agent_index):
            Returns a list of legal actions for an agent
            agent_index=0 means our agent, the opponent is agent_index=1

        Action.STOP:
            The stop direction, which is always legal

        game_state.generate_successor(agent_index, action):
            Returns the successor game state after an agent takes an action
        """
        leagl_actions = game_state.get_legal_actions(0)
        arr = [(action, self.__min_max_value(game_state.generate_successor(
            0, action), 2*self.depth - 1, True)) for action in leagl_actions]
        return max(arr, key=lambda x: x[1])[0]

    def __min_max_value(self, game_state, depth, is_min=True):
        if depth == 0 or game_state.done:
            return self.evaluation_function(game_state)
        leagl_actions = game_state.get_legal_actions(is_min)
        arr = [self.__min_max_value(game_state.generate_successor(
            is_min, action), depth - 1, not is_min) for action in leagl_actions]
        if is_min:
            return min(arr)
        return max(arr)


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def get_action(self, game_state):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        """*** YOUR CODE HERE ***"""
        leagl_actions = game_state.get_legal_actions(0)
        alpha = float('-inf')
        beta = float('inf')
        best_action = None
        for action in leagl_actions:
            v = self.__min_helper(game_state.generate_successor(
                0, action), 2*self.depth - 1, alpha, beta)
            if alpha < v:
                alpha = v
                best_action = action
        return best_action

    def __max_helper(self, game_state, depth, alpha, beta):
        if depth == 0 or game_state.done:
            return self.evaluation_function(game_state)
        leagl_actions = game_state.get_legal_actions(0)
        v = float('-inf')
        for action in leagl_actions:
            v = max(v, self.__min_helper(
                game_state.generate_successor(0, action), depth - 1, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def __min_helper(self, game_state, depth, alpha, beta):
        if depth == 0 or game_state.done:
            return self.evaluation_function(game_state)
        leagl_actions = game_state.get_legal_actions(1)
        v = float('inf')
        for action in leagl_actions:
            v = min(v, self.__max_helper(
                game_state.generate_successor(1, action), depth - 1, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
    Your expectimax agent (question 4)
    """

    def get_action(self, game_state):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        The opponent should be modeled as choosing uniformly at random from their
        legal moves.
        """
        """*** YOUR CODE HERE ***"""
        leagl_actions = game_state.get_legal_actions(0)
        best_action = None
        alpha = float('-inf')
        for action in leagl_actions:
            v = self.__expect_helper(game_state.generate_successor(
                0, action), 2*self.depth - 1)
            if alpha < v:
                alpha = v
                best_action = action
        return best_action

    def __max_helper(self, game_state, depth):
        if depth == 0 or game_state.done:
            return self.evaluation_function(game_state)
        leagl_actions = game_state.get_legal_actions(0)
        v = float('-inf')
        for action in leagl_actions:
            v = max(v, self.__expect_helper(
                game_state.generate_successor(0, action), depth - 1))
        return v

    def __expect_helper(self, game_state, depth):
        if depth == 0 or game_state.done:
            return self.evaluation_function(game_state)
        leagl_actions = game_state.get_legal_actions(1)
        v = 0
        for action in leagl_actions:
            v += self.__max_helper(
                game_state.generate_successor(1, action), depth - 1)
        return v/len(leagl_actions)

weights = np.array([[24, 26, 28, 30],
                    [22, 20, 18, 16],
                    [8, 10, 12, 14],
                    [6, 4, 2, 1]]).flatten()
weights2 = np.array([[1, 14, 16, 30],
                    [2, 12, 18, 28],
                    [4, 10, 20, 26],
                    [6, 8, 22, 24]]).flatten()
weights3 = np.rot90(weights.reshape(4, 4), k=1).flatten()
weights4 = np.rot90(weights2.reshape(4, 4), k=1).flatten()
weights5 = np.rot90(weights3.reshape(4, 4), k=1).flatten()
weights6 = np.rot90(weights4.reshape(4, 4), k=1).flatten()
weights7 = np.rot90(weights5.reshape(4, 4), k=1).flatten()
weights8 = np.rot90(weights6.reshape(4, 4), k=1).flatten()

def better_evaluation_function(current_game_state):
    """
    Your extreme 2048 evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    # return current_game_state.score + np.exp(len(current_game_state.get_empty_tiles())) + current_game_state.max_tile
    # currently best

    # features = np.array([current_game_state.score, len(current_game_state.get_empty_tiles()), current_game_state.max_tile,
    #                      current_game_state.board[0][0], current_game_state.board[0][
    #                          3], current_game_state.board[3][0], current_game_state.board[3][3],
    #                     current_game_state.board[0][1], current_game_state.board[1][0]])
    # weights = np.array([8, 4, 2, 3, 0, 0, 0, 1, 1])  # 20
    
    features = current_game_state.board.flatten()
    max_value = max(np.dot(features, weights),np.dot(features, weights2),np.dot(features, weights3),
                np.dot(features, weights4),np.dot(features, weights5),np.dot(features, weights6),
                np.dot(features, weights7),np.dot(features, weights8))

    return max_value + current_game_state.score
    # return current_game_state.score + len(current_game_state.get_empty_tiles())


# Abbreviation
better = better_evaluation_function
