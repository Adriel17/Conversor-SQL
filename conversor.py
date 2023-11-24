import pandas as pd

#data = pd.read_csv(r'C:\Users\Ron\Desktop\Test\products.csv')
data = pd.read_excel("tablela.xlsx").to_csv("tabelacsv.csv",index=None, header=True)

df = pd.DataFrame(data)
print(df)