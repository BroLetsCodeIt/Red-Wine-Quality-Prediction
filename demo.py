import pandas as pd 
import numpy as np 
 
df = pd.read_csv('./dataset/winequality-red.csv') 

ans = df.head()
print(ans)