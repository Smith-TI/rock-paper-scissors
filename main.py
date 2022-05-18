from factory import MoveFactory


def main():
    move_factory = MoveFactory()

    rock = move_factory.create_rock()
    paper = move_factory.create_paper()
    scissor = move_factory.create_scissor()

    print(rock.play_against(rock))
    print(rock.play_against(paper))
    print(rock.play_against(scissor))


if __name__ == '__main__':
    main()
