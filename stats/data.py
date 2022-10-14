import os
import glob
import pandas as pd

game_files=glob.glob(os.path.join(os.getcwd(),'games','*.EVE'))
game_files.sort()

game_frames=[]
for game_file in game_files:
    game_frame= pd.read_csv(game_file,names=['type', 'multi2', 'multi3','multi4', 'multi5', 'multi6','event'])
    game_frames.append(game_frame)

# Pandas appending data frames
games = pd.concat(game_frames)

# Pandas change values `loc`
games.loc[games['multi5'] == '??', 'multi5'] = ''

#   Pandas string methods (extract)
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')

#   Pandas fill empty 'cells' `fillna` with forward fill
identifiers = identifiers.fillna(method='ffill')

#   Pandas `columns` property
identifiers.columns = ['game_id', 'year']

#   Pandas appending data frames
games = pd.concat([games, identifiers], axis=1, sort=False)

#   Pandas fill empty 'cells' `fillna`
games = games.fillna(' ')

#   Pandas enum
games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])

games.head()
