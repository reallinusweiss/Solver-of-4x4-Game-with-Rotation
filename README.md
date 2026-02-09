# Solver-of-4x4-Game-with-Rotation
This Script prints out the best possible move of a 4x4 Game with the Following Rules:
Player 1 (Red) and Player 2 (Black) both have 8 stones each. The game board has 4x4 squares, and the goal of each player
is to connect 4 stones in a straight line, so vertical, horizontal or diagonally, after they finish their move with the Rotation-Button.
Player 1 starts by placing a stone of him on any square and finishes his move by pressing the Rotate-Button.
The Rotate-Button rotates every stone counter-clockwise. After that the player 2 has to move one of player 1 stones, that is on the game board
on any empty square. Then he has to place one of his stones (which are not on the game board) on any empty square and finish his move with the Rotation-Button.
Since Player 2 has now one stone on the Game Board, Player 1 now also has to move one of the stones of player 2, and the game continues until no stones are left.
If both players connect 4 stones in a straight line, or if the game board is full with neither player connecting 4 stones (after player 2 finishes his move by pressing
the Rotation-Button) the players draw.

To create the data that the solver works, the files 1-5 has to be executed in order from 1-5. Since the Files 1-5 depend on each other, files 2 can only be executed after file 1 and so on.
It takes at least an hour to compute all the data, and you need at least 16 GB of RAM.
After that is done, the File Solver.py can be executed and you can select the game board you want to solve. For storage efficiency only possible game states are stored, so 
game states that are not possible to reach are impossible to solve.
