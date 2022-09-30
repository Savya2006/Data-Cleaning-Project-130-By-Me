import csv
import pandas as pd

df=pd.read_csv("total_stars.csv")

print(df.shape) #Will give us no. of rows and columns
print(list(df)) # Gives us the header list

del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]


df = df.rename({
                'Mass': "Weight", 
                'Luminisity': "Shining Capacity", 
            }, axis='columns')


df.to_csv("final.csv")

print(df.shape) #Will give us no. of rows and columns
print(list(df)) # Gives us the header list