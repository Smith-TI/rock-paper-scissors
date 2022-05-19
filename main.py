from factory import MoveFactory
from players import Player


def main():
    move_factory = MoveFactory()

    rock = move_factory.create_rock()
    paper = move_factory.create_paper()
    scissor = move_factory.create_scissor()

    print(" <<<<<<<<< Normal game >>>>>>>>> ")
    print(rock.play_against(rock))
    print(rock.play_against(paper))
    print(rock.play_against(scissor))

    random_move1 = move_factory.create_random()
    random_move2 = move_factory.create_random()
    print()
    print(" <<<<<<<<< Random Moves >>>>>>>> ")
    print(random_move1.play_against(random_move2))

    player1 = Player()
    player2 = Player()

    print()
    print(" <<<<<<<<< Player Games >>>>>>>> ")
    print("Player 1 vs Player 2")

    player1.select_random_move()
    player2.select_random_move()
    player1.play_against(player2)

    player1.select_move('rock')
    player2.select_move('scissor')
    player1.play_against(player2)

    player1.select_random_move()
    player2.select_random_move()
    player1.play_against(player2)

    player1.select_mirror_move(opponent=player2)
    player2.select_random_move()
    player1.play_against(player2)


if __name__ == '__main__':
    main()
