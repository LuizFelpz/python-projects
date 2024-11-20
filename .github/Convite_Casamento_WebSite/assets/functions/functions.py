import pandas as pd
import random as rd

dt = pd.read_csv(r'assets\database\Convidados.csv', delimiter= ',', encoding = 'latin')


cdg = 'e56Ac'

dt.replace(dt.loc[dt['Cdg_Convite'] == cdg, 'Confirmado'], value = 'True', inplace = False)

print(dt)



