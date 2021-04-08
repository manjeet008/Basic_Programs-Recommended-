import pandas as pd
df=pd.read_csv('INPUT.csv')
df.to_excel('OUTPUT.xlsx','sheet1')