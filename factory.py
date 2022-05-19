import random
from game import Rock, Paper, Scissor
from interfaces import MoveStrategyFactoryInterface
from strategies import RockStrategy, PaperStrategy, ScissorStrategy


class MoveStrategyFactory(MoveStrategyFactoryInterface):
    def create_rock_strategy(self) -> RockStrategy:
        return RockStrategy()

    def create_paper_strategy(self) -> PaperStrategy:
        return PaperStrategy()

    def create_scissor_strategy(self) -> ScissorStrategy:
        return ScissorStrategy()


class MoveFactory:
    def __init__(self) -> None:
        self.game_strategy_factory = MoveStrategyFactory()

    def create_rock(self):
        return Rock(self.game_strategy_factory.create_rock_strategy())

    def create_paper(self):
        return Paper(self.game_strategy_factory.create_paper_strategy())

    def create_scissor(self):
        return Scissor(self.game_strategy_factory.create_scissor_strategy())

    def create_random(self):
        return random.choice([
            self.create_rock(),
            self.create_paper(),
            self.create_scissor()
        ])
