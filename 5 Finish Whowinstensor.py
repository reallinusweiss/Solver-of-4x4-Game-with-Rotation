import numpy as np
import pickle

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "Boardgametensor"

for i in range(15,0,-1):
    print(i)
    whowins_tensor = np.stack(np.load(DATA_DIR / f"whowins_tensor{i+1}.npz", allow_pickle=True)['arr_0'])
    whowins_tensor_new = np.stack(np.load(DATA_DIR / f"whowins_tensor{i}.npz", allow_pickle=True)['arr_0'])
    game_paths = np.stack(np.load(DATA_DIR / f'game_paths_{i}.npz', allow_pickle=True)['arr_0'])
    print(len(game_paths))
    print(len(whowins_tensor_new))

    if i % 2 == 0:
    #player 1 turn
        for u in range(len(game_paths)):
            whowins_new_array = whowins_tensor_new[u]
            whowins_array = whowins_tensor[game_paths[u]]
            if whowins_new_array[0] == 100:
                if 1 in whowins_array[:,0]:
                    smallest = min(whowins_array[whowins_array[:,0]==1,1])
                    whowins_tensor_new[u] = [1, smallest+1]
                elif 0 in whowins_array[:,0]:
                    smallest = min(whowins_array[whowins_array[:,0]==0,1])
                    whowins_tensor_new[u] = [0, smallest+1]
                else: 
                    biggest = max(whowins_array[whowins_array[:,0]==2,1])
                    whowins_tensor_new[u] = [2, biggest+1]
        np.savez_compressed(DATA_DIR / f'whowins_tensor{i}.npz', whowins_tensor_new)
    else:
    #player 2 turn
        for u in range(len(game_paths)):
            whowins_new_array = whowins_tensor_new[u]
            whowins_array = whowins_tensor[game_paths[u]]
            if whowins_new_array[0] == 100:
                if 2 in whowins_array[:,0]:
                    smallest = min(whowins_array[whowins_array[:,0]==2,1])
                    whowins_tensor_new[u] = [2, smallest+1]
                elif 0 in whowins_array[:,0]:
                    smallest = min(whowins_array[whowins_array[:,0]==0,1])
                    whowins_tensor_new[u] = [0, smallest+1]
                else: 
                    biggest = max(whowins_array[whowins_array[:,0]==1,1])
                    whowins_tensor_new[u] = [1, biggest+1]
        np.savez_compressed(DATA_DIR / f'whowins_tensor{i}.npz', whowins_tensor_new)