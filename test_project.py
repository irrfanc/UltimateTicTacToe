from project import game_grid, checkWin, best_move

def test_game_grid():
    grid_size = 3
    grid = game_grid(grid_size)
    assert len(grid) == grid_size * grid_size
    for cell in grid:
        assert cell == " "

def test_checkWin():
    grid_size = 3
    #winning condition
    grid = ["X", "O", "X", "X", "O", " ", "X", " ", " "]
    assert checkWin(grid, "X", grid_size)

    # non-winning condition
    grid = ["X", "O", "X", "X", "O", " ", " ", " ", " "]
    assert not checkWin(grid, "X", grid_size)

def test_best_move():
    # difficulty = easy
    grid_size = 3
    grid = ["X", "O", "X", "X", "O", " ", " ", " ", " "]
    difficulty = "E"
    best_move_result = best_move(grid, grid_size, difficulty)
    assert best_move_result in [5, 6, 7, 8]
