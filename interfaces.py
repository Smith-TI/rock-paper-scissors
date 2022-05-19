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


class PlayerInterface:
    def select_move(self, move):
        pass

    def select_random_move(self):
        pass

    def select_mirror_move(self, opponent):
        pass

    def get_current_move(self):
        pass

    def get_previous_move(self):
        pass

    def add_move_to_history(self, move):
        pass

    def play_against(self, opponent):
        pass
