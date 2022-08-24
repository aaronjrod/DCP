class GameState:
    def __init__(self, grid = [[0 for x in range(7)] for x in range(6)], turn = False) -> None:
        self.grid = grid
        # False: Means its black's turn to play
        self.turn = turn
        self.over = False
        print(self)

    def __str__(self) -> str:
        out = "Turn of Player " + str(self.turn+1) + "\n"
        for row in self.grid:
            out += str(row) + "\n"
        return out

    def is_valid(self, row, col):
        if 0 > row or row >= len(self.grid):
            return False
        if 0 > col or col >= len(self.grid[row]):
            return False
        return True
    
    def is_occupied(self, row, col):
        return self.grid[row][col] != 0

    def next_turn(self, col):
        if not self.is_valid(0, col):
            return 
        if self.is_occupied(0, col):
            return 

        row = len(self.grid)-1
        while self.is_occupied(row, col):
            row -= 1
        
        p_num = self.turn+1
        self.grid[row][col] = p_num
        self.turn = not self.turn

        self.over = self.check_end_condition(row, col, p_num)
        print(self)

    # idea: if a previous state has a successful end condition, then this
    # wouldn't even be called. So, only check around the most recent move.
    def check_end_condition(self, row, col, p_num):
        directions = [  (-1, -1), (-1, 1),
                        (0, -1), (0, 1),
                        (1, -1), (1, 0), (1, 1)]
        
        for next in directions:
            count = 1
            row_t = row + next[0]
            col_t = col + next[1]
            while self.is_valid(row_t, col_t):
                if self.grid[row_t][col_t] != p_num:
                    break
                count += 1
                row_t += next[0]
                col_t += next[1]
            if count >= 4:
                return True
        return False
 
board = GameState()
while not board.over:
    col = input()
    if not str.isdigit(col):
        continue
    board.next_turn(int(col)-1)
print("game over!")
print("Winner is player " + str(2-board.turn))