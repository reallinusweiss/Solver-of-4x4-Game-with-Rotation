import numpy as np
import pickle 

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "Boardgametensor"

player = 0
rotation_index = np.array([1,2,3,7,0,6,10,11,4,5,9,15,8,12,13,14])
rotation_index_backwards = np.argsort(rotation_index)




for i in range(16):
    print(i)
    #load Hashindex
    boardgame_hashindex = np.load(DATA_DIR / f'game_tensor_hashindex_{i+1}.npz')
    keys = boardgame_hashindex['keys']
    values = boardgame_hashindex['values']


    powers_of_3 = 3**np.arange(16, dtype=np.int32)                  
    keys = np.dot(keys[:,rotation_index_backwards], powers_of_3)


    boardgame_hashindex = dict(zip(keys, values))

    #create an array of the positions of both player pieces
    boardgame_tensor = np.stack(np.load(DATA_DIR / f'game_tensor_small_{i+1}.npz', allow_pickle=True)['arr_0'])
    if i % 2 == 0:
        player = 2
        notplayer = 1
        notplayeramount = int((i+2)/2)
    else:
        player = 1
        notplayer = 2
        notplayeramount = int((i+1)/2)
    playerturns = int((i+2)/2)
    boardgame_paths = np.empty([len(boardgame_tensor)], dtype=object)
    for j in range(len(boardgame_tensor)):
        paths = []
        boardgame = np.array(boardgame_tensor[j],dtype='int8')
        playernotplayingpositions = np.where(boardgame==notplayer)
        emptypositions = np.where(boardgame==0)
        boardgame = np.dot(boardgame, powers_of_3)

        #loop to choose every opponent piece
        for index_k,k in enumerate(playernotplayingpositions[0]):
            #remove opponent piece
            boardgame = boardgame - (notplayer*powers_of_3[k])

            #loop to place opponent piece
            for index_l,l in enumerate(emptypositions[0]):
                #place removed opponent piece
                boardgame = boardgame + (notplayer*powers_of_3[l])
                #create new empty array 
                emptypositions_2 = emptypositions[0].copy()
                emptypositions_2[index_l] = k
                #loop to place own piece
                for m in emptypositions_2:
                    #place own piece
                    boardgame = boardgame + (player*powers_of_3[m])
                    #add path of possible move to array
                    paths.append(boardgame_hashindex[boardgame])
                    boardgame = boardgame - (player*powers_of_3[m])
                    #reset own placed piece
                boardgame = boardgame - (notplayer*powers_of_3[l])
                #reset moved opponent piece
            boardgame = boardgame + (notplayer*powers_of_3[k])
            #reset removed opponent piece
        boardgame_paths[j] = np.array(paths, dtype='int32')
    np.savez_compressed(DATA_DIR / f'game_paths_{i+1}.npz', boardgame_paths)