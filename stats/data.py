import os
import glob
import pandas as pd

game_files=glob.glob(os.path.join(os.getcwd(),'games','*.EVE'))
game_files.sort()

for game_file in game_files:
    game_frame= pd.read_csv(game_file)
    
