def find_king(board):
    king_pos = None
    king_count = 0
    for r, row_str in enumerate(board):
        for c, char in enumerate(row_str):
            if char == 'K':
                king_pos = (r, c)
                king_count += 1
    if king_count == 1:
        return king_pos
    return None

def is_valid_board(board):
    """ตรวจสอบว่ากระดานเป็นสี่เหลี่ยมจัตุรัสมั้ย"""
    if not board:
        return False
    rows = len(board)
    for row_str in board:
        if len(row_str) != rows:
            return False
    return True

def checkmate(board):
    """ตรวจสอบความถูกต้องของกระดาน"""
    if not is_valid_board(board):
        print("Fail")
        return

    """หาตำแหน่งคิง"""
    king_pos = find_king(board)
    if not king_pos:
        print("Fail")
        return

    king_r, king_c = king_pos
    size = len(board)

    """วนลูปเพื่อหาตัวหมากศัตรูทั้งหมด"""
    for r, row_str in enumerate(board):
        for c, piece in enumerate(row_str):
            is_threat = False
            
            """ตรวจ Pawn"""
            if piece == 'P':
                """Pawnจะรุกเมื่ออยู่แนวทแยงที่ติดกับคิง"""
                if abs(r - king_r) == 1 and abs(c - king_c) == 1:
                    is_threat = True

            """ตรวจ Rook, Queen ในแนวตั้งและแนวนอน"""
            if piece in 'RQ':
                """ตรวจแนวนอน"""
                if r == king_r:
                    path_clear = True
                    start, end = min(c, king_c), max(c, king_c)
                    for i in range(start + 1, end):
                        if board[r][i] != '.':
                            path_clear = False
                            break
                    if path_clear:
                        is_threat = True
                
                """ตรวจแนวตั้ง"""
                if c == king_c and not is_threat:
                    path_clear = True
                    start, end = min(r, king_r), max(r, king_r)
                    for i in range(start + 1, end):
                        if board[i][c] != '.':
                            path_clear = False
                            break
                    if path_clear:
                        is_threat = True

            """ตรวจ Bishop, Queen ในแนวทแยง"""
            if piece in 'BQ': 
                """ตรวจแนวทแยง"""
                if abs(r - king_r) == abs(c - king_c):
                    path_clear = True
                    step_r = 1 if king_r > r else -1
                    step_c = 1 if king_c > c else -1
                    curr_r, curr_c = r + step_r, c + step_c
                    while curr_r != king_r:
                        if board[curr_r][curr_c] != '.':
                            path_clear = False
                            break
                        curr_r += step_r
                        curr_c += step_c
                    if path_clear:
                        is_threat = True
            
            """ถ้ารุกได้แสดง Success แล้วจบการทำงาน"""
            if is_threat:
                print("Success")
                return

    """วนลูปจนจบแล้วรุกไม่ได้"""
    print("Fail")