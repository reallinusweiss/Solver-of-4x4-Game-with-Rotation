import numpy as np

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "Boardgametensor"

for i in range(15):
    boardgametensor_hash_index = {}
    boardgametensor = np.stack(np.load(DATA_DIR / f'game_tensor_small_{i+2}.npz', allow_pickle=True)['arr_0'])
    for position, wert in enumerate(boardgametensor):
        boardgametensor_hash_index[tuple(wert)] = position
    np.savez_compressed(f'Boardgametensor/game_tensor_hashindex_{i+1}.npz',
        keys=np.array(list(boardgametensor_hash_index.keys()), dtype='int8'),
        values=np.array(list(boardgametensor_hash_index.values()), dtype='int32'))
    

