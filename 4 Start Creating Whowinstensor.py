import numpy as np

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "Boardgametensor"

#check for game end
def check_end(boardgametensor,i, whowins_tensor, l):
    playerwin = [False, False]
    for u in range(1,3):
        for o in range(4):
            if boardgametensor[0+o*4] == u and boardgametensor[1+o*4] == u and boardgametensor[2+o*4] == u and boardgametensor[3+o*4] == u:
                playerwin[u-1] = True
        for o in range(4):
            if boardgametensor[0+o] == u and boardgametensor[4+o] == u and boardgametensor[8+o] == u and boardgametensor[12+o] == u: 
                playerwin[u-1] = True
        if boardgametensor[0] == u and boardgametensor[5] == u and boardgametensor[10] == u and boardgametensor[15] == u:
            playerwin[u-1] = True
        if boardgametensor[3] == u and boardgametensor[6] == u and boardgametensor[9] == u and boardgametensor[12] == u:
            playerwin[u-1] = True
    if playerwin[0]:
        if playerwin[1]:
            whowins_tensor[l][0] = 0
            whowins_tensor[l][1] = 0
        else:
            whowins_tensor[l][0] = 1
            whowins_tensor[l][1] = 0
    elif playerwin[1]:
        whowins_tensor[l][0] = 2
        whowins_tensor[l][1] = 0
    elif i==16:
        whowins_tensor[l][0] = 0
        whowins_tensor[l][1] = 0


for i in range(16,0,-1):
    #boardgame = np.genfromtxt(f"Boardgametensor/game_tensor_small_{i}.csv", delimiter=",", dtype = 'int8', ndmin=2)
    boardgame = np.stack(np.load(DATA_DIR / f'game_tensor_small_{i}.npz', allow_pickle=True)['arr_0'])

    whowins_tensor = np.empty([len(boardgame),2],dtype='int8')
    whowins_tensor.fill(100)
    if i >= 7:
        for l in range(len(boardgame)):
            boardgametensor = boardgame[l]
            check_end(boardgametensor,i, whowins_tensor, l)
    np.savez_compressed(DATA_DIR / f'whowins_tensor{i}.npz', whowins_tensor, dtype='int8')



