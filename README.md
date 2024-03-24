# Ultimate Tic Tac Toe Game

#### Video Demo: https://youtu.be/Y65t6zJAO3w

#### Description:
This project is called Ultimate Tic Tac Toe. On executing the code and it prompts the user for either Player vs player or Player vs bot game mode. The PvP is just your usual tic tac toe game where User can play 1 on 1 but now the user can choose if they want to play in a 3x3 grid or a 4x4 grid. The real fun is with the bot vs player mode. It asks the user for the difficulty level, either easy medium or hard.

#### Features
-Two different type of grids (3x3, 4x4) which adds fun into the usual tic tac toe game.
-Multiplayer. The user can play with a friend or an AI bot.
-Different difficulty levels.

## functions
- Printing the board: The code begins by printing the board. The functions "game_grid(grid_size)" and "display_grid(grid, grid_size)" are responsible for printing the board. I've kept the printing dynamic so it can print both 3x3 grids and 4x4 grid.
- The function checkWin(grid, player, grid_size) defines the win conditions by rows, colums and diagons and append them into a list to check for later
if a person has won based on the condition in the list. I've implemented the function in a dynamic way so that it can define both 3x3 and 4x4 win conditions
- Function is_grid_full(grid) checks if the board is full which will help was determine if a game results in a draw
- evaluate_grid(grid, player, grid_size) takes in 3 arguements and helps us to evaluate the ongoing game state which will help us in the bot strategic decision making.
-The minimax function is where the bot moves are defined. I debated whether to use Monte Carlo Tree Search MCTS or Minimax but for a game of tic tac toe with only two player I went for minimax with alpha beta pruning which reduces the number of nodes in the search tree which is a little efficient for 4x4 grids and takes less time to process.
-best_move function finds the best move for the bot, we start by defining the worst possible score for the bot and work our way up from there. This function also takes in consideration the difficulty level of the game by setting the depth of the search tree to 1 for easy level, 3 for medium and 6 for high level. The choice for these particular depth was somewhat trial and error and I found them apt for the given conditions.
- In game_mode is the code which asks the user wether he/she wants to play PvP or vs bot.
- PvP if the function where human player to human player code is defined. It ask the player to make the game move and also manages the printing for the game won, input validation and updating the grid.
-game_play manage the flow of the game and determines the game's outcome based on the chosen game mode and bot difficulty.
-And finally in the main section of the script starts the game by asking the user to choose game mode, grid size, and bot difficulty


## How to Play:

1. Execute the file to start the game.
2. Type the game mode "e" for easy, "m" for medium and "h" for hard difficulty
3. Choose the grid size, either grid of 3x3 or 4x4.
4. The difficulty level can be selected if the user chooses Bot mode.
5. The instructions are printed at the beginning of the game.

## AI Difficulty Levels:

- **Easy:** User can type "E" for this level. This level uses less depth for the search tree and hence it's easy to win
- **Medium:** "M" to choose the medium mode. It becomes more challanging to beat the bot at this level but it's not impossible
- **Hard:** "H" for hard mode. At the level it's almost impossible to beat the bot

## Additional Information:

- The game displays the grid with numbers which the user can input to make their moves.
- If the user thinks the game will end in a draw, just type "exit" during their turn.
- If a player wins or if the game is draw the game ends.

