import pandas as pd
import plotly.express as px
import numpy as np

df=pd.read_csv('D:\project\class106\Student Marks vs Days Present.csv')
c=df['Days Present'].tolist()
hs=df['Marks In Percentage'].tolist()

fig=px.scatter(df,x='Days Present',y='Marks In Percentage')
fig.show()
correlation=np.corrcoef(x=c,y=hs)

print(correlation[0][1])