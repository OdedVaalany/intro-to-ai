from board import Board
from search import SearchProblem, ucs
import util


class BlokusFillProblem(SearchProblem):
    """
    A one-player Blokus game as a search problem.
    This problem is implemented for you. You should NOT change it!
    """

    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0)):
        self.board = Board(board_w, board_h, 1, piece_list, starting_point)
        self.expanded = 0

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def is_goal_state(self, state):
        """
        state: Search state
        Returns True if and only if the state is a valid goal state
        """
        return not any(state.pieces[0])

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        # Note that for the search problem, there is only one player - #0
        self.expanded = self.expanded + 1
        return [(state.do_move(0, move), move, 1) for move in state.get_legal_moves(0)]

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        return len(actions)


#####################################################
# This portion is incomplete.  Time to write code!  #
#####################################################
class BlokusCornersProblem(SearchProblem):
    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0)):
        self.expanded = 0
        self.board = Board(board_w, board_h, 1, piece_list, starting_point)

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def is_goal_state(self, state):
        return sum(state.state[([0, 0, -1, -1], [0, -1, 0, -1])] == [0, 0, 0, 0]) >= 4

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        # Note that for the search problem, there is only one player - #0
        self.expanded = self.expanded + 1
        return [(state.do_move(0, move), move, move.piece.get_num_tiles()) for move in state.get_legal_moves(
            0) if self.__valid_step(state, move)]

    def __valid_step(self, state, move):
        new_state = state.do_move(0, move)
        if new_state.state[0, 0] == -1 and (new_state.state[0, 1] == 0 or new_state.state[1, 0] == 0):
            return False
        if new_state.state[0, -1] == -1 and (new_state.state[0, -2] == 0 or new_state.state[1, -1] == 0):
            return False
        if new_state.state[-1, -1] == -1 and (new_state.state[-1, -2] == 0 or new_state.state[-2, -1] == 0):
            return False
        if new_state.state[-1, 0] == -1 and (new_state.state[-1, 1] == 0 or new_state.state[-2, 0] == 0):
            return False

        return True

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        return sum([action.piece.get_num_tiles() for action in actions]) 


def blokus_corners_heuristic(state, problem):
    """
    Your heuristic for the BlokusCornersProblem goes here.

    This heuristic must be consistent to ensure correctness.  First, try to come up
    with an admissible heuristic; almost all admissible heuristics will be consistent
    as well.

    If using A* ever finds a solution that is worse uniform cost search finds,
    your heuristic is *not* consistent, and probably not admissible!  On the other hand,
    inadmissible or inconsistent heuristics may find optimal solutions, so be careful.
    """
    # return problem.get_cost_of_actions(state.get_legal_moves(0))  # works good on a small board
    # This is supposed to be the best heuristic |  Expanded nodes: 9668, score: 17
    return 4 - sum(state.state[([0, 0, -1, -1], [0, -1, 0, -1])] == [0, 0, 0, 0])


class BlokusCoverProblem(SearchProblem):
    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0), targets=[(0, 0)]):
        self.targets = targets.copy()
        self.expanded = 0
        self.board = Board(board_w, board_h, 1, piece_list, starting_point)

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def is_goal_state(self, state):
        if all(state.state[y, x] == 0 for y, x in self.targets):
            return True

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        # Note that for the search problem, there is only one player - #0
        self.expanded = self.expanded + 1
        return [(state.do_move(0, move), move, move.piece.get_num_tiles())
                for move in state.get_legal_moves(0) if self.__is_valid_step(state, move)]

    def __is_valid_step(self, state, move):
        w, h = state.board_w, state.board_h
        to_check = self.targets[:]
        to_check += [(y-1, x-1)
                     for y, x in self.targets if y - 1 >= 0 and x - 1 >= 0]
        to_check += [(y+1, x-1)
                     for y, x in self.targets if y + 1 < h and x - 1 >= 0]
        new_state = state.do_move(0, move)
        for y, x in to_check:
            if new_state.state[y, x] == -1 and (
                    new_state.state[y, max(x - 1, 0)] == 0 or new_state.state[y, min(x + 1, w-1)] == 0 or new_state.state[
                        max(y - 1, 0), x] == 0 or new_state.state[min(y + 1, h-1), x] == 0
            ):
                return False
        to_check = self.targets[:]
        to_check += [(y-1, x+1)
                     for y, x in self.targets if y - 1 >= 0 and x + 1 < 0]
        to_check += [(y+1, x+1)
                     for y, x in self.targets if y + 1 < h and x + 1 < 0]
        new_state = state.do_move(0, move)
        for y, x in to_check:
            if new_state.state[y, x] == -1 and (
                    new_state.state[y, max(x - 1, 0)] == 0 or new_state.state[y, min(x + 1, w-1)] == 0 or new_state.state[
                        max(y - 1, 0), x] == 0 or new_state.state[min(y + 1, h-1), x] == 0
            ):
                return False

        return True

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        return sum([action.piece.get_num_tiles() for action in actions]) 


def blokus_cover_heuristic(state, problem):
    return sum(state.state[y, x] == -1 for y, x in problem.targets)
