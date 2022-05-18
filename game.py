from interfaces import MoveStrategyInterface, MoveInterface


class Move(MoveInterface):
    def __init__(self) -> None:
        self.set_move_strategy(None)

    def __init__(self, strategy) -> None:
        self.set_move_strategy(strategy)

    def set_move_strategy(self, strategy: MoveStrategyInterface):
        self.strategy = strategy

    def get_move_strategy(self) -> MoveStrategyInterface:
        return self.strategy


class Rock(Move):

    def __init__(self, strategy) -> None:
        super().__init__(strategy)

    def __str__(self) -> str:
        return f"Rock! 🪨"


class Paper(Move):

    def __init__(self, strategy) -> None:
        super().__init__(strategy)

    def __str__(self) -> str:
        return f"Paper! 📜"


class Scissor(Move):

    def __init__(self, strategy) -> None:
        super().__init__(strategy)

    def __str__(self) -> str:
        return f"Scissor! ✂️"
