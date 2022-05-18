class Move:
    def __init__(self) -> None:
        pass


class Rock(Move):
    def __str__(self) -> str:
        return f"Rock! 🪨"


class Paper(Move):
    def __str__(self) -> str:
        return f"Paper! 📜"


class Scissor(Move):
    def __str__(self) -> str:
        return f"Scissor! ✂️"


class MoveFactory:

    def create_rock(self) -> Rock:
        return Rock()

    def create_paper(self) -> Paper:
        return Paper()

    def create_scissor(self) -> Scissor:
        return Scissor()


def game():
    move_factory = MoveFactory()

    rock = move_factory.create_rock()
    paper = move_factory.create_paper()
    scissor = move_factory.create_scissor()

    print(rock, paper, scissor)


if __name__ == '__main__':
    game()
