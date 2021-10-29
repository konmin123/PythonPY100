EMPTY_CELL = "-"

def get_ferst_player():

def is_win(field) -> bool :
    win_combinations = [
        [(1,1),(1,2),(1,3)],
        [(2,1),(2,2),(2,3)],
        [(3,1),(3,2),(3,3)],

        [(1,1),(2,1),(3,1)],
        [(1,2),(2,2),(3,2)],
        [(1,3),(2,3),(3,3)],

        [(1,1),(2,2),(3,3)],
        [(1,3),(2,2),(3,1)],
    ]

    for win_comb in win_combinations:
        row_index = win_comb[0][0]
        col_index = win_comb[0][1]
        cell_ = field[row_index][col_index]

def is_available_cell(field) -> bool:
    for row in field:
        for cell in row:
            if cell == EMPTY_CELL:
                return True
    return False

def init_field(size=3):
    field = [
        [EMPTY_CELL for _ in range(size)]
        for _ in range(size)
    ]
    return field

def is_empty_cell(field: list,x: int ,y : int) -> bool:
    cell = field[x][y]
    # if cell == EMPTY_CELL:
    #     return  True
    # else:
    #     return False
    return  True if cell == EMPTY_CELL else False