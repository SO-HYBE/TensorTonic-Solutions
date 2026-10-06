import numpy as np

def go_group_liberties(board: list, row: int, col: int) -> tuple:
    """
    Returns: a tuple of two sorted coordinate lists: group and liberties.
    """

    np_board = np.array(board)
    height, width = np_board.shape
    
    color = np_board[row, col]
    if color == 0:
        return ([], [])

    group = set()
    liberties = set()
    stack = [(row, col)]
    visited = set()

    while stack:
        r, c = stack.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        group.add((r, c))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width:
                neighbor_val = np_board[nr, nc]
                if neighbor_val == color and (nr, nc) not in visited:
                    stack.append((nr, nc))
                elif neighbor_val == 0:
                    liberties.add((nr, nc))

    sorted_group = sorted(list(group), key=lambda x: (x[0], x[1]))
    sorted_liberties = sorted(list(liberties), key=lambda x: (x[0], x[1]))

    return (sorted_group, sorted_liberties)

            