def game_grid(grid_size):
    return [" " for _ in range(grid_size * grid_size)]


def display_grid(grid, grid_size):
    for row in range(grid_size):
        for column in range(grid_size):
            print(grid[row * grid_size + column], end="")
            if column < grid_size - 1:
                print(" | ", end="")
        print()
        if row < grid_size - 1:
            print("-" * (4 * grid_size - 1))


def checkWin(grid, player, grid_size):
    win_conditions = []

    for i in range(grid_size):
        win_conditions.append([j for j in range(i * grid_size, (i + 1) * grid_size)])

    for i in range(grid_size):
        win_conditions.append([j for j in range(i, grid_size**2, grid_size)])

    win_conditions.append([i for i in range(0, grid_size**2, grid_size + 1)])
    win_conditions.append(
        [i for i in range(grid_size - 1, grid_size**2 - 1, grid_size - 1)]
    )

    for condition in win_conditions:
        if all(grid[i] == player for i in condition):
            return True
    return False


def is_grid_full(grid):
    return " " not in grid


def evaluate_grid(grid, player, grid_size):
    if checkWin(grid, "O", grid_size):
        return 1  # bot wins
    elif checkWin(grid, "X", grid_size):
        return -1  # Player wins
    elif is_grid_full(grid):
        return 0  # draw
    return 0  # No one won yet


def minimax(grid, depth, player, grid_size, alpha, beta):
    if (
        depth == 0
        or checkWin(grid, "O", grid_size)
        or checkWin(grid, "X", grid_size)
        or is_grid_full(grid)
    ):
        return evaluate_grid(grid, player, grid_size)

    if player == "O":
        max_eval = -float("inf")
        for move in range(grid_size**2):
            if grid[move] == " ":
                grid[move] = player
                eval = minimax(grid, depth - 1, "X", grid_size, alpha, beta)
                grid[move] = " "
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float("inf")
        for move in range(grid_size**2):
            if grid[move] == " ":
                grid[move] = player
                eval = minimax(grid, depth - 1, "O", grid_size, alpha, beta)
                grid[move] = " "
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval


EASY_DEPTH = 1
MEDIUM_DEPTH = 3
HARD_DEPTH = 6


def best_move(grid, grid_size, difficulty):
    best_move = None
    best_eval = -float("inf")

    if difficulty == "E":
        depth = EASY_DEPTH
    elif difficulty == "M":
        depth = MEDIUM_DEPTH
    elif difficulty == "H":
        depth = HARD_DEPTH
    else:
        raise ValueError(
            "Invalid difficulty level. Please choose 'E' for easy, 'M' for medium, 'H' for hard."
        )

    for move in range(grid_size**2):
        if grid[move] == " ":
            grid[move] = "O"
            eval = minimax(grid, depth, "X", grid_size, -float("inf"), float("inf"))
            grid[move] = " "
            if eval > best_eval:
                best_eval = eval
                best_move = move
    return best_move


def game_mode():
    print("Welcome to Ultimate Tic Tac Toe!")
    print("Choose the game mode:")
    print("1. Player vs. Player")
    print("2. Player vs. BOT")

    while True:
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            return "PvP"
        elif choice == "2":
            return "PvAI"
        else:
            print("Invalid choice. Please enter 1 or 2")


def PvP(grid_size):
    grid = game_grid(grid_size)
    current_player = "X"

    while True:
        display_grid(grid, grid_size)

        if checkWin(grid, current_player, grid_size):
            display_grid(grid, grid_size)
            print(f"Player {current_player} wins!")
            break

        while True:
            try:
                player_move = input(
                    f"Enter Player {current_player}'s move (1-{grid_size ** 2}): "
                )
                print()
                if player_move.lower() == "exit":
                    print("Exiting the game. Adios!")
                    return
                player_move = int(player_move) - 1
                if 0 <= player_move < grid_size**2 and grid[player_move] == " ":
                    grid[player_move] = current_player
                    if checkWin(grid, current_player, grid_size):
                        display_grid(grid, grid_size)
                        print(f"Player {current_player} wins!")
                        return
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print(
                    f"Invalid input. Enter a number between 1 and {grid_size ** 2} or 'exit' to quit the game."
                )

        current_player = "O" if current_player == "X" else "X"

    if is_grid_full(grid):
        display_grid(grid, grid_size)
        print("It's a draw!")


def game_play(grid_size, game_mode, difficulty):
    if game_mode == "PvP":
        PvP(grid_size)
    else:
        grid = game_grid(grid_size)
        current_player = "X"

        while True:
            display_grid(grid, grid_size)
            print()

            if checkWin(grid, current_player, grid_size):
                display_grid(grid, grid_size)
                print(f"Player {current_player} wins!")
                break

            if current_player == "X":
                while True:
                    try:
                        player_move = input(
                            f"Enter Player {current_player}'s move (1-{grid_size ** 2}): "
                        )
                        if player_move.lower() == "exit":
                            print("Exiting the game. Adios!")
                            return
                        player_move = int(player_move) - 1
                        if (
                            0 <= player_move < grid_size**2
                            and grid[player_move] == " "
                        ):
                            grid[player_move] = "X"
                            if checkWin(grid, "X", grid_size):
                                display_grid(grid, grid_size)
                                print("Player X wins!")
                                print()
                                return
                            break
                        else:
                            print("Invalid move. Try again.")
                    except ValueError:
                        print(
                            f"Invalid input. Enter a number between 1 and {grid_size ** 2} or 'exit' to quit the game."
                        )
                current_player = "O"
            else:
                ai_best_move = best_move(grid, grid_size, difficulty)
                if ai_best_move is not None:
                    row = ai_best_move // grid_size
                    col = ai_best_move % grid_size
                    if (
                        0 <= row < grid_size
                        and 0 <= col < grid_size
                        and grid[row * grid_size + col] == " "
                    ):
                        grid[row * grid_size + col] = "O"
                        if checkWin(grid, "O", grid_size):
                            display_grid(grid, grid_size)
                            print("Player O wins!")
                            return
                current_player = "X"

            if is_grid_full(grid):
                display_grid(grid, grid_size)
                print("It's a draw!")


if __name__ == "__main__":
    game_mode = game_mode()
    while True:
        grid_size = input("Choose the grid size (3 for 3x3 grid, 4 for 4x4 grid): ")
        if grid_size == "3" or grid_size == "4":
            grid_size = int(grid_size)
            break
        else:
            print("Invalid choice. Please enter 3 or 4")

    if grid_size == 3 or grid_size == 4:
        if game_mode == "PvAI":
            print("Choose difficulty:")
            print("E for easy")
            print("M for medium")
            print("H for hard")
            print("To exit, type 'exit' at any time.")
            print()
        while True:
            if grid_size == 3:
                print("Instructions:")
                print("1 | 2 | 3")
                print("---------")
                print("4 | 5 | 6")
                print("---------")
                print("7 | 8 | 9")
                print()
            elif grid_size == 4:
                print("Instructions:")
                print("1 |  2 | 3  | 4")
                print("------------------")
                print("5 |  6 | 7  | 8")
                print("------------------")
                print("9 | 10 | 11 | 12")
                print("------------------")
                print("13| 14 | 15 | 16")
                print()
            if game_mode == "PvAI":
                difficulty = input("Enter your choice: ").upper()

                if difficulty in ["E", "M", "H"]:
                    game_play(grid_size, game_mode, difficulty)
                    break
            else:
                game_play(grid_size, game_mode, None)
                break
            if difficulty == "EXIT":
                print("Exiting the game. Goodbye!")
                break
            else:
                print(
                    "Invalid choice. Please choose 'E' for easy, 'M' for medium, 'H' for hard, or 'EXIT' to quit the game."
                )
    else:
        print("Invalid grid size. Please choose 3 or 4.")
