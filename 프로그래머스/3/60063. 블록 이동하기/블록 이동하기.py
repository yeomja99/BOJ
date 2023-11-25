from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    x1, y1, x2, y2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # 상하좌우
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]
        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]
        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_pos.append({(nx1, ny1), (nx2, ny2)})
    # 회전
    # 가로로 놓여있는 경우
    if x1 == x2:
        for i in [-1, 1]:
            if board[x1+i][y1] == 0 and board[x1+i][y2] == 0:
                next_pos.append({(x1, y1), (x1+i,y1)})
                next_pos.append({(x2, y2), (x1+i,y2)})
    # 세로로 놓여있는 경우
    elif y1 == y2:
        for i in [-1, 1]:
            if board[x1][y1+i] == 0 and board[x2][y1+i] == 0:
                next_pos.append({(x1, y1), (x1, y2+i)})
                next_pos.append({(x2, y2), (x2, y1+i)})
    return next_pos
        

def solution(board):
    answer = 0
    q = deque()
    n = len(board)
    pos = {(1,1), (1,2)}
    q.append((pos,0))
    visit = []
    visit.append(pos)
    
    new_board = [[1 for x in range(n+2)]for x in range(n+2)]
    for i in range(1, n+1):
        for j in range(1,n+1):
            new_board[i][j] = board[i-1][j-1]
    
    while q:
        pos, d = q.popleft()
        if (n, n) in pos: return d
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visit:
                visit.append(next_pos)
                q.append((next_pos, d+1))
                
    
    return answer