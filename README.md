# rock-paper-scissors

Assignment for Design Patterns Lecture

# Problem

    Design a rock-scissors-paper game pattern that allows two different move types.
    You must be able to change the move type in the runtime.
    - Random Move: showing a random hand signal.
    - Mirror Move: showing a hand signal from the previous opponent's hand signal.

# Solution

### Assumptions

- This game will be played between `two players` per turn.

### Let's start by analysing the game:

1. **Game rules:**

- Rock > Scissors
- Scissors > Paper
- Paper > Rock
- Rock = Rock
- Paper = Paper
- Scissors = Scissors

2. **Game Entities:**

- Current Player 1 Move
- Current Player 2 Move
- Previous Opponent Moves of Player 1
- Previous Opponent Moves of Player 2
- Rock Move
- Paper Move
- Scissor Move

3. **Game Interactions:**

- Play Random Move
- Play Mirror Move
- Interactions between different moves


### Design Pattern:

- We see that each move has different behaviour when interacting with different moves.
- All these interactions must be implemented in their own class to make sure that the open/close principle is followed.

- We also have a need to create different moves based on what is requested (random move, mirror move, etc.) 
- I simply choose the `factory` design pattern for creation of these moves as it seems the most apt.