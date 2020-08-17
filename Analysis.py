import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv('student.csv')
mean = df.groupby(['student_id','Level'],as_index=False)['Attempt'].mean()

fig = px.scatter(mean,x="student_id",y="Level",size="Attempt",color="Attempt")

fig.show()