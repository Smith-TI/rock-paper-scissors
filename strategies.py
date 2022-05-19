from interfaces import MoveStrategyInterface
from game import Rock, Paper, Scissor


class RockStrategy(MoveStrategyInterface):
    def play(self, hand) -> int:
        if isinstance(hand, Rock):
            return 'draw'
        if isinstance(hand, Paper):
            return 'lose'
        if isinstance(hand, Scissor):
            return 'win'
        raise ValueError(f'Move {hand} is Invalid!')


class PaperStrategy(MoveStrategyInterface):
    def play(self, hand) -> int:
        if isinstance(hand, Paper):
            return 'draw'
        if isinstance(hand, Scissor):
            return 'lose'
        if isinstance(hand, Rock):
            return 'win'
        raise ValueError(f'Move {hand} is Invalid!')


class ScissorStrategy(MoveStrategyInterface):
    def play(self, hand) -> int:
        if isinstance(hand, Scissor):
            return 'draw'
        if isinstance(hand, Rock):
            return 'lose'
        if isinstance(hand, Paper):
            return 'win'
        raise ValueError(f'Move {hand} is Invalid!')

