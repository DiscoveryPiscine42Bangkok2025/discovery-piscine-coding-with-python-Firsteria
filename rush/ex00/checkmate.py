rook_dirs   = [(0,1),(0,-1),(1,0),(-1,0)]
bishop_dirs = [(1,1),(1,-1),(-1,1),(-1,-1)]
queen_dirs  = rook_dirs + bishop_dirs

def king_position(board):
    """Find the position of the King on the board"""
    lines = board.strip().split('\n')
    for r, row in enumerate(lines):
        for c, piece in enumerate(row):
            if piece == 'K':
                return r, c
    return None

def is_valid(r, c, lines):
    """Check if position is inside the board"""
    return 0 <= r < len(lines) and 0 <= c < len(lines[0])

def check_sliding_attack(king_r, king_c, lines, attackers, directions):
    """
    Generic function for Rook, Bishop, Queen.
    attackers = set(['R']), set(['B']), or set(['Q'])
    directions = list of (dr, dc)
    """
    for dr, dc in directions:
        r, c = king_r + dr, king_c + dc
        while is_valid(r, c, lines):
            piece = lines[r][c]
            if piece in attackers:
                return True
            elif piece not in ('.', ' '):  # blocked
                break
            r, c = r + dr, c + dc
    return False

def check_pawn_attack(king_r, king_c, lines):
    """Check if Pawn attacks King (downward only in this version)"""
    for dr, dc in [(1, -1), (1, 1)]:
        r, c = king_r + dr, king_c + dc
        if is_valid(r, c, lines) and lines[r][c] == 'P':
            return True
    return False

def checkmate(board):
    try:
        #no king checker
        king = king_position(board)
        if not king:
            print("Fail"); return
        kr, kc = king
        
        #check board is square
        lines = board.strip().split('\n')
        n = len(lines)
        if any(len(line) != n for line in lines):
            print("Fail"); return
        
        #no input 
        if not board or not board.strip():
            print("Fail"); return
        
        #check attack successs
        if (check_pawn_attack(kr, kc, lines) or
            check_sliding_attack(kr, kc, lines, {'R'}, rook_dirs) or
            check_sliding_attack(kr, kc, lines, {'B'}, bishop_dirs) or
            check_sliding_attack(kr, kc, lines, {'Q'}, queen_dirs)):
            print("Success")
        else:
            print("Fail")
    except Exception:
        print("Fail")
