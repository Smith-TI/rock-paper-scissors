class MoveStrategyInterface:
    # Interface
    def play(self, move) -> str:
        pass


class MoveInterface:
    # Interface
    def set_move_strategy(self, strategy: MoveStrategyInterface):
        pass

    def get_move_strategy(self) -> MoveStrategyInterface:
        pass

    def play_against(self, move):
        print(f'{self}  vs {move}', end="   ")
        return self.get_move_strategy().play(move)


class MoveStrategyFactoryInterface:
    # Interface
    def create_rock_strategy(self) -> MoveStrategyInterface:
        pass

    def create_paper_strategy(self) -> MoveStrategyInterface:
        pass

    def create_scissor_strategy(self) -> MoveStrategyInterface:
        pass
