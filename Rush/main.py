def find_king(board):
    #Find the king Positions
    lines = board.strip().split('\n')
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == 'K':
                return row, col
    return None