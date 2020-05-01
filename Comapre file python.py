import pandas as pd
import numpy as np
import datacompy

 
df1=pd.read_csv('file1.csv', na_values=['NA'])
df2=pd.read_csv('file2.csv', na_values=['NA'])

df1.sort_values(by ='CITY' , inplace=True, ascending=False)
df2.sort_values(by ='CITY' , inplace=True, ascending=False)
   
print (" Rows in df1")
row = df1.shape[0]
print(row)
       
print (" Columns in df1")

col = df1.shape[1]

print(col)


print ("Rows in df2")
rowcount = df2.shape[0]
print(rowcount)
       
print ("Columns in df2")

olcount = df2.shape[1]

print(colcount)


df1.equals(df2)
similar-values = df1.values == df2.values
print (similar-values)


rows,cols=np.where(similar-values==False)

for item in zip(rows,cols):
   df1.iloc[item[0], item[1]] = '{} --> {}'.format(df1.iloc[item[0], item[1]],df2.iloc[item[0], item[1]])
  

output= (df1.reset_index(drop=True) == df2.reset_index(drop=True))| df1.reset_index(drop=True).isnull()==df2.reset_index(drop=True).isnull()

output['Unmatched Values']=df2.CITY

output['diff']=out.sum(int(True))-df2.CITY
 





# diffrent method


df2['version'] = "file1"
df1['version'] = "file2"

file1 = set(df2['CITY'])
file2 = set(df1['CITY'])
Diff_Values = file1 - file2
new_Values = file2 - file2


Adding_files = pd.concat([df1,df2],ignore_index=True)
changes = Adding_files.drop_duplicates(subset=["A","B","C"], keep=False)

diff_Vlaues = changes[changes['CITY'].duplicated() == True]['CITY'].tolist()
diff = changes[changes["CITY"].isin(diff_Vlaues)]

New = diff[(diff["version"] == "file1")]
Old = diff[(diff["version"] == "file2")]

New = New.drop(['version'], axis=1)
Old = Old.drop(['version'], axis=1)

New.set_index('City', inplace=True)
Old.set_index('City', inplace=True)

changes = pd.concat([Old, New],
                            axis='columns',
                            keys=['file1', 'file2'],
                            join='outer')


def Diffrent_val(x):
    return x[0] if x[0] == x[1] else '{} ---> {}'.format(*x)


changes = changes.swaplevel(axis='columns')[New.columns[0:]]

df_Diff = changes.groupby(level=0, axis=1).apply(lambda frame: frame.apply(Diffrent_val, axis=1))
df_Diff = df_Diff.reset_index()

df_difff = changes[changes["CITY"].isin(Diff_Values)]
df_new = changes[changes["CITY"].isin(new_Values)]

output_columns = ["A","B","C"]
writer = pd.ExcelWriter("outout.xlsx")
df_Diff.to_excel(writer,"Changes")
df_difff.to_excel(writer,"Deleted")
df_new.to_excel(writer,"New")
df1.to_excel(writer,"Diffrenance")
out.to_excel(writer,"To compare line by line")

writer.save()
