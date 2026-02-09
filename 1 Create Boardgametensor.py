import numpy as np


from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "Boardgametensor"
DATA_DIR.mkdir(exist_ok=True)

gameboard = np.array([0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0],dtype='int8')
gameboard_array = []
gameboard_array.append(gameboard.copy())


#create all combinations of 0, 1 and 2
def flip_loop(flip_pos):
    if gameboard[flip_pos] != 2:
        gameboard[flip_pos] = gameboard[flip_pos] + 1
        gameboard_array.append(gameboard.copy())
    else:
        gameboard[flip_pos] = 0
        flip_pos = flip_pos - 1
        flip_loop(flip_pos)

for i in range(3**16):
    flip_pos = 15
    flip_loop(flip_pos)

gameboard_array = np.array(gameboard_array, dtype='int8')

#Change Array to Tensor to make to possible to store which round the game is in
zero_count = np.sum(gameboard_array == 0, axis=1, dtype='int8')
for i in range(16):
    gameboard_tensor = gameboard_array[zero_count == (15-i)]

    #remove most impossible games
    one_correct_amount = int((i+2)/2)
    two_correct_amount = int((i+1)/2)
    count_ones = np.sum(gameboard_tensor == 1, axis=1, dtype='int8')
    count_twos = np.sum(gameboard_tensor == 2, axis=1, dtype='int8')
    keep_list = (count_ones == one_correct_amount) + (count_twos == two_correct_amount)
    gameboard_tensor = gameboard_tensor[keep_list]
    np.savez_compressed(DATA_DIR / f'game_tensor_small_{i+1}.npz', gameboard_tensor, gameboard_tensor)
