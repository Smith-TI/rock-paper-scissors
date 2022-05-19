import re
from typing import Union

from game import Paper, Rock, Scissor
from interfaces import PlayerInterface
from factory import MoveFactory


class Player(PlayerInterface):
    def __init__(self) -> None:
        self.current_move = None
        self.previous_moves = []

    def select_move(self, move):
        move_factory = MoveFactory()
        self.current_move = move_factory.create_move(move)

    def select_random_move(self):
        move_factory = MoveFactory()
        self.current_move = move_factory.create_random()

    def select_mirror_move(self, opponent: PlayerInterface):
        self.current_move = opponent.get_previous_move()

    def get_current_move(self) -> Union[Rock, Paper, Scissor]:
        if(self.current_move):
            return self.current_move
        return self.select_random_move()

    def get_previous_move(self):
        if(len(self.previous_moves) != 0):
            return self.previous_moves[-1]
        raise IndexError('No previous moves!')

    def add_move_to_history(self, move):
        self.previous_moves.append(move)

    def play_against(self, opponent: PlayerInterface):
        my_move = self.get_current_move()
        opponent_move = opponent.get_current_move()
        # print(f'[log] my_move: {my_move}, opponent_move: {opponent_move}')
        print(my_move.play_against(opponent_move))
        self.add_move_to_history(move=my_move)
        opponent.add_move_to_history(move=opponent_move)
