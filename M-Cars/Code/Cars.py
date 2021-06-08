from search import Problem

import math

#am utilizat code_skeleton -ul de la problema puzzle 15 pe care l-am adaptat pe cerinte

class Cars(Problem):

    def __init__(self, initial: object, marime_parcare: object, goal=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,0)):
        """ Define goal state and initialize a problem """
        self.goal = goal
        self.numar_curent = 0
        self.marime_parcare = marime_parcare
        Problem.__init__(self, initial, goal)

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""
        if self.numar_curent <= self.marime_parcare:
            self.numar_curent += 1

        if self.numar_curent == self.marime_parcare + 1:
            self.numar_curent = 1

        return state.index(self.numar_curent)

    def actions(self, state):
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'STAY', 'JUMPLEFT', 'JUMPRIGHT', 'JUMPUP', 'JUMPDOWN']
        self.index = self.find_blank_square(state)
        if state[self.index] == self.goal[self.index]:
            possible_actions.remove('LEFT')
            possible_actions.remove('UP')
            possible_actions.remove('RIGHT')
            possible_actions.remove('DOWN')
            possible_actions.remove('JUMPLEFT')
            possible_actions.remove('JUMPUP')
            possible_actions.remove('JUMPRIGHT')
            possible_actions.remove('JUMPDOWN')
            return possible_actions
        if self.index % self.marime_parcare == 0 or state[self.index - 1] != 0:
            possible_actions.remove('LEFT')

        if self.index % self.marime_parcare <= 1 or state[self.index - 2] != 0 or state[self.index - 1] == 0:
            possible_actions.remove('JUMPLEFT')

        if self.index < self.marime_parcare or state[self.index - self.marime_parcare] != 0:
            possible_actions.remove('UP')

        if self.index < 2 * self.marime_parcare or state[self.index - 2 * self.marime_parcare] != 0 or state[self.index - self.marime_parcare] == 0 :
            possible_actions.remove('JUMPUP')

        if self.index % self.marime_parcare == self.marime_parcare - 1 or state[self.index + 1] != 0:
            possible_actions.remove('RIGHT')

        if self.index % self.marime_parcare >= self.marime_parcare - 2 or state[self.index + 2] != 0 or state[self.index + 1] == 0:
            possible_actions.remove('JUMPRIGHT')

        if self.index > (pow(self.marime_parcare, 2) - self.marime_parcare - 1) or state[self.index + self.marime_parcare] != 0:
            possible_actions.remove('DOWN')

        if self.index > (pow(self.marime_parcare, 2) - 2 * self.marime_parcare - 1) or state[self.index + self.marime_parcare] == 0 or state[self.index + 2 * self.marime_parcare] != 0:
            possible_actions.remove('JUMPDOWN')
               
        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """
        new_state = list(state)
        delta = {'UP': -self.marime_parcare, 'DOWN': self.marime_parcare, 'LEFT':-1, 'RIGHT':1, 'STAY':0, 'JUMPLEFT':-2, 'JUMPRIGHT':2, 'JUMPDOWN':+ 2 * self.marime_parcare, 'JUMPUP':- 2 * self.marime_parcare }
        neighbor = self.index + delta[action]
        new_state[self.index], new_state[neighbor] = new_state[neighbor], new_state[self.index] 

        return tuple(new_state)

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))


#euristica Manhattan

class CarsMht(Cars):
    def h(self, node):

        dim = self.marime_parcare
        return sum( ( abs(int(s / dim) - int(g / dim)) + abs(int(s % dim) - int(g % dim)) ) for (s,g) in zip (node.state, self.goal) )
class CarsMiss(Cars):
    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = number of misplaced tiles """
        return sum(s != g for (s, g) in zip(node.state, self.goal))
