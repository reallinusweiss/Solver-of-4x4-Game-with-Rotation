import tkinter as tk
import numpy as np
from pathlib import Path
np.set_printoptions(threshold=np.inf)

BASE_DIR = Path(__file__).resolve().parent





root = tk.Tk()
root.title('16 Buttons')

colour = "white"
buttons = []

boardgame = np.zeros([16], dtype='int8')
rotation_index = np.array([1,2,3,7,0,6,10,11,4,5,9,15,8,12,13,14])
rotation_index_backwards = np.argsort(rotation_index)


def button_click(n,buttons, colour):
    #change buttons correctly
    global boardgame
    boardgame[n] = boardgame[n] + 1
    if boardgame[n] == 1:
        colour = "red"
    if boardgame[n] == 2:
        colour = "black"
    if boardgame[n] > 2:
        boardgame[n] = 0
        colour = "SystemButtonFace"
    buttons[n].config(text=boardgame[n], bg=colour)

def show_moves():
    global boardgame
    i = np.count_nonzero(boardgame)
    game_paths = np.stack(np.load(BASE_DIR / f'Boardgametensor/game_paths_{i}.npz', allow_pickle=True)['arr_0'])
    whowins_tensor = np.stack(np.load(BASE_DIR / f"Boardgametensor/whowins_tensor{i+1}.npz", allow_pickle=True)['arr_0'])
    boardgametensor = np.stack(np.load(BASE_DIR / f"Boardgametensor/game_tensor_small_{i}.npz", allow_pickle=True)['arr_0'])
    boardgametensor2 = np.stack(np.load(BASE_DIR / f"Boardgametensor/game_tensor_small_{i+1}.npz", allow_pickle=True)['arr_0'])
    print("test")
    u = np.where(np.all(boardgametensor == boardgame, axis=1))[0]
    whowins_array = np.squeeze(whowins_tensor[game_paths[u]])
    game_path = np.squeeze(game_paths[u])
    if i % 2 == 0:
    #player 1 turn
        #player 1 wins
        if 1 in whowins_array[:,0]:
            #pick the smallest round out of the winning paths 
            smallest = min(whowins_array[whowins_array[:,0]==1,1])
            #check the indexes of the winning paths, convert that into that into winning parts,
            #and convert that into the winning moves
            moves = boardgametensor2[game_path[np.all(whowins_array == [1,smallest], axis=1)]]
            moves = moves[:,rotation_index_backwards]
            print(moves.reshape(moves.shape[0],4,4))
            print(f'Player 1 wins in {smallest} moves')
        #player 1 draws
        elif 0 in whowins_array[:,0]:
            biggest = min(whowins_array[whowins_array[:,0]==0,1])
            moves = boardgametensor2[game_path[np.all(whowins_array == [0,biggest], axis=1)]]
            moves = moves[:,rotation_index_backwards]
            print(moves.reshape(moves.shape[0],4,4))
            print(f'Player 1 draws in {biggest} moves')
        #player 1 looses
        else: 
            biggest = max(whowins_array[whowins_array[:,0]==2,1])
            moves = boardgametensor2[game_path[np.all(whowins_array == [2,biggest], axis=1)]]
            moves = moves[:,rotation_index_backwards]
            print(moves.reshape(moves.shape[0],4,4))
            print(f'Player 1 looses in {biggest} moves')
    else:
    #player 2 turn
        #player 2 wins
        if 2 in whowins_array[:,0]:
            smallest = min(whowins_array[whowins_array[:,0]==2,1])
            moves = boardgametensor2[game_path[np.all(whowins_array == [2,smallest], axis=1)]]
            moves = moves[:,rotation_index_backwards]
            print(moves.reshape(moves.shape[0],4,4))
            print(f'Player 2 wins in {smallest} moves')

        #player 2 draws 
        elif 0 in whowins_array[:,0]:
            biggest = min(whowins_array[whowins_array[:,0]==0,1])
            moves = boardgametensor2[game_path[np.all(whowins_array == [0,biggest], axis=1)]]
            moves = moves[:,rotation_index_backwards]
            print(moves.reshape(moves.shape[0],4,4))
            print(f'Player 2 draws in {biggest} moves')


        #player 2 looses
        else: 
            biggest = max(whowins_array[whowins_array[:,0]==1,1])
            moves = boardgametensor2[game_path[np.all(whowins_array == [1,biggest], axis=1)]]
            moves = moves[:,rotation_index_backwards]
            print(moves.reshape(moves.shape[0],4,4))
            print(f'Player 2 looses in {biggest} moves')

def rotate():
    global boardgame
    boardgame_torotate = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], dtype = 'int8')
    colourarray = np.empty(16, dtype='object')
    for i in range(16): 
        boardgame_torotate[i]= buttons[i]['text']
        colourarray[i]= buttons[i]['bg']
    boardgame_torotate = boardgame_torotate[rotation_index]
    colourarray = colourarray[rotation_index]
    for i in range(16): 
        buttons[i].config(text=boardgame_torotate[i], bg=colourarray[i])
    boardgame = boardgame_torotate




for i in range(16):
    btn = tk.Button(root, text=0, command= lambda n=i: button_click(n,buttons, colour), bg = "SystemButtonFace")
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    buttons.append(btn)


btn_pfct = tk.Button(root, text ="perfect Moves", command=  show_moves)
btn_rt = tk.Button(root, text ="rotate", command = rotate)
btn_pfct.grid(row=4, column=0, columnspan=4, pady=10)
btn_rt.grid(row=4, column=4, columnspan=4, pady=10)
root.mainloop()