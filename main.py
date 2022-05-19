from factory import MoveFactory


def main():
    move_factory = MoveFactory()

    rock = move_factory.create_rock()
    paper = move_factory.create_paper()
    scissor = move_factory.create_scissor()

    random_move1 = move_factory.create_random()
    random_move2 = move_factory.create_random()

    print(" <<<<<<<<< Normal game >>>>>>>>> ")
    print(rock.play_against(rock))
    print(rock.play_against(paper))
    print(rock.play_against(scissor))
    print()
    print(" <<<<<<<<< Random Moves >>>>>>>> ")
    print(random_move1.play_against(random_move2))


if __name__ == '__main__':
    main()
