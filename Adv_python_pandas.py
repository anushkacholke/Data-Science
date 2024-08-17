# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 19:43:44 2024

@author: Sai
"""

########################3series (1-D) data structure in pandas
import pandas as pd
x=[3,5,6,7,8]
var = pd.Series(x)
print(var)
print(type(var))
print(var[2])
#changing index
var=pd.Series(x,index=['a','b','c','d','e'])
print(var)
#dtype parameter used to change the datatype & name parameter used to give the name to the dataset
var=pd.Series(x,index=['a','b','c','d','e'],dtype="float",name="python")
print(var)

#we can also used diff. types of data set like tuple,set,dictionary etc
dic={"name":["java","cpp",'c','python'],"rank":[1,2,3,4]}
var1=pd.Series(dic)
print(var1)
var1=pd.Series(dic,name="dictionary_dataSet")   
var1
print(type(var))
   ##dtype: object ::  here dtype is object bez we can used mixed data like dictionary,list 

s=pd.Series(12)
print(s)
print(type(s))
s=pd.Series(12,index=(1,2,3,4,5))
s

s1=pd.Series(12,index=(1,2,3,4,5))
s2=pd.Series(12,index=(1,2,3))
print(s1+s2)


###################DataFrame (2-D) data structure in python pandas 
import pandas as pd
l=[1,2,3,4,5,6]
var=pd.DataFrame(l)
print(var)
print(type(var))
#dataFrame using dictionary
import pandas as pd
dic={"a":[1,2,3],"b":[11,22,33]}
var1=pd.DataFrame(dic)
print(var1)
print(type(var1))
var1=pd.DataFrame(dic,columns=["a"],index=["a","b","c"])
print(var1)
var1=pd.DataFrame(dic)
print(var1)
print(var1["a"][2])   #it display column a of index[2] value So, output is: 3

list1=[[11,22,33,44,55],[1,2,3,4,5]]
var2=pd.DataFrame(list1)
print(var2)

# It combine 2 series to create one dataframe
sr={"s":pd.Series([1,2,3,4]),"r":pd.Series([1,2,3,4])}
var3=pd.DataFrame(sr)
print(var3)
print(type(var3))

################Arithmatic operations in pandas
import pandas as pd
var=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
var
var["C"]=var["A"]+var["B"]     #adition
var['D']=var['A']-var['B']      #subtraction
var['E']=var['A']/var['B']      #division
var['F']=var['A']*var['B']      #multiplication
var

var1=pd.DataFrame({'a':[11,22,33],'b':[10,20,30]})
var1['c']=var1['a'] <= 20
print(var1)

#Insert in python pandas using insert()function
import pandas as pd
var=pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8]})
var
var.insert(1,'python',var['A'])
var
var.insert(3,'java',[12,13,14,15])
var

#############Delete in python pandas using pop() function and del keyword
var=pd.DataFrame({'A':[1,2,3,4],'B':[5,6,7,8],'C':[99,88,77,66]})
var
var1=var.pop('B')
print(var1)
del var["A"]
var

######################write CSV file
import pandas as pd
dis={'a':[1,2,3,4],'b':[11,22,33,44],'c':[10,20,30,40]}
d=pd.DataFrame(dis)
d
d.to_csv("Test_new.csv")
d.to_csv("Test.csv",index=False,header=[1,2,3])

############################Read CSV
import pandas as pd
csv_1=pd.read_csv("C:\\Users\\Sai\\Test.csv")
csv_1
#read perticular row by passing row no.
csv_1=pd.read_csv("C:\\Users\\Sai\\Test.csv",nrows=(1))
csv_1
print(type(csv_1))
#read perticular column by passing column no. or index no.
csv_1=pd.read_csv("C:\\Users\\Sai\\Test.csv",usecols=[1])
csv_1
#skip perticular row by passing row no.
csv_1=pd.read_csv("C:\\Users\\Sai\\Test.csv",skiprows=(1))
csv_1
#it change the order of index here 1st index 1 is displya then 0 , 2 ,3 ....
csv_1=pd.read_csv("C:\\Users\\Sai\\Test.csv",index_col=(1))
csv_1
#if you want to change the header  Here 2 nd row becomes a header
csv_1=pd.read_csv("C:\\Users\\Sai\\Test.csv",header=2)
csv_1
#name parameter use to give name to the header
csv_1=pd.read_csv("C:\\Users\\Sai\\Test.csv",names=["col1","col2","col3"])
csv_1
#remove header by assinging None
csv_1=pd.read_csv("C:\\Users\\Sai\\Test.csv",header=None)
csv_1

################################Pandas Function
import pandas as pd
csv_1=pd.read_csv("C:\\Users\\Sai\\Test.csv")
csv_1
#return index no.
csv_1.index
#return colums names
csv_1.columns
#describe()
csv_1.describe()
#head() return starting 2 data
csv_1.head(2)
#tail() return ending 2 data
csv_1.tail(2)
#it disply data from index 0 to 2-1 it is like a string slicing
csv_1[:2]
csv_1[1:3]
print(type(csv_1))
#display index  no. as an array also display length and dtype
csv_1.index.array
#it convert DataFrame into numpy to array
csv_1.to_numpy()
#2nd option for converting DataFrame into  numpy to array
import numpy as np
v=np.asarray(csv_1)
v
#it sort the data in reverse order and 0 for rows and 1 for column
csv_1.sort_index(axis=0,ascending=False)

csv_1=[1][0]="py"
csv_1
print(csv_1)

csv_1.loc[0,[1]]='py'
csv_1
#used to caugth perticuler data
csv_1.loc[[3],[1]]
#it display perticular index data
csv_1.iloc[0,1]
#drop() delete column 1 bez axis is 1(and you know 1 for column)
csv_1.drop(1,axis=1)

##############################dropna & fillna
##dropna
var = pd.read_csv("C:\\Users\\Sai\\Test.csv")
var
#dropna() drop the NaN(missing) data and we can also drop as axis
var.dropna()
#how="any" remove missing values
var.dropna(how="any")
#it remove whole row which has missing data
var.dropna(how="all")
#subset parameter drop perticuler column null values
var.dropna(subset=[2])
#replace parameter remove null values and create new data set
var.dropna(inplace=True)
var
#if any row has single null value then it will drop that row if the multiple null values then it doesn't drop
var.dropna(thresh=1)   #here I assign 1 so it delete that row where only 1 null value

##fillna
#value parameter give the value of null values here all null values are assign by "python"
var.fillna(value="python")
#forword fill the data from same as like above & backword fill the data same as like below
var.fillna(method="bfill")
var.fillna(method="ffill")
#inplace create the replacing file of orignal file all null values are replace by 12
var.fillna(12,inplace=True)
var

#####################Handling missing values(Replace & Interpolat)
####Replace
import pandas as pd
var = pd.read_csv("C:\\Users\\Sai\\Test.csv")
var
#it replace any value to new value
var.replace(to_replace=1,value=22)
#it replace all serial no. to 22
var.replace([0,1,2,3],22)
#here all 1 replace  by python
var.replace([1],"python",regex=True)
#here replace dictionary data between 1-10 by 22
var.replace({0:[1-10]},22,regex=True)
var.replace(1,method="ffill")
#here 11.0 are replace by forword fill and it only replace 2 values bez we set limit 2
var.replace(11.0,method="ffill",limit=2)

####Iterpolate - It automatically fill the data squencially We not neet to give data
import pandas as pd
#I will just create one csv file here#
dic={'a':["java",'python','cpp'],'b':['math','phy','chem'],'c':['account','sci','comm']}
d=pd.DataFrame(dic)
d                                              
d1=d.to_csv("new.csv")
d1
var1 = pd.read_csv("C:\\Users\\Sai\\new.csv")
var1
var
## 
#interpolate() only works on numbers
var.interpolate()
#it fill data in linearly 
var.interpolate(method="linear",axies=1)   #1 for row and 0 for cloumn
#only 2 data are fill bez we set limit as 2
var.interpolate(limit=2)
# also fill data directionally: forward, backward, both
var.interpolate(limit_direction="backward",limit=2)

#####################Merging and concat in python pandas
####Merge
import pandas as pd
var1=pd.DataFrame({'A':[1,2,3,4],'B':[11,22,33,44]})
var1
var2=pd.DataFrame({'A':[1,2,3,5],'C':[21,31,41,51]})
var2
#merge based on A bez A is common in both
pd.merge(var1, var2,on = 'A')
#how parameter reprsent missing data
pd.merge(var1, var2,how='inner')  #fill inner missing data
pd.merge(var1, var2,how='left')   #fill left missing data 
pd.merge(var1, var2,how = 'right') # fill right missing data3
pd.merge(var1, var2,left_index=True,right_index=True,suffixes=("name","id"))

####concat: 2 dataframes and series
#concate 2 series
sr1=pd.Series([1,2,3,4])
sr2=pd.Series([21,31,41,51])
sr1
sr2
pd.concat([sr1,sr2])
#concate 2 dataframes
d1=pd.DataFrame({'A':[1,2,3,4],'B':[11,22,33,44]})
d2=pd.DataFrame({'A':[1,2,3,5],'C':[21,31,41,51]})
pd.concat([d1,d2])
pd.concat([d1,d2],axis=1)
pd.concat([d1,d2],axis=0)

pd.concat([d1,d2],axis=1,join="inner")
pd.concat([d1,d2],axis=1,join="outer")
pd.concat([d1,d2],axis=1,keys=["var1","var2"])

####################groupby in python pandas
import pandas as pd
var1=pd.DataFrame({'name':['a','b','c','d','a','b','a','b','a','c','c','d'],"s_1":[12,13,14,12,13,14,15,23,25,16,10,34],"s_2":[23,24,25,26,27,28,29,30,25,34,35,56]})
var1
var_new=var1.groupby("name")    # group by data according to name 
var_new
for x,y in var_new:
    print(x)
    print(y)

#it display all 'a' data
var_new.get_group("a")
#display all min data of a,b,c,d
var_new.min()
var_new.max()   #display all max data of a,b,c,d
var_new.mean()  #display all mean data of a,b,c,d

######################join and append in python pandas
import pandas as pd
##join()
var1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
var2=pd.DataFrame({"C":[10,20,30,40],"D":[21,31,41,51]})
var1.join(var2)
var1.join(var2,how="left")
var1.join(var2,how="right")
var1.join(var2,how="inner")
var1.join(var2,how="outer")
##append()
var1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
var2=pd.DataFrame({"C":[10,20,30,40],"D":[21,31,41,51]})
var1.append(var2)

var1.append(var2,ignore_index=True)

####################pivot table and melt function in python pandas
#####melt()
var1=pd.DataFrame({"days":[1,2,3,4,5,6],"eng":[10,12,14,15,16,12],"math":[17,18,19,23,34,12]})
var1
#melt() it display table vertically
pd.melt(var1)
pd.melt(var1,id_vars=["days"],var_name="python")
######privot() : used for data arranging shaping
var1=pd.DataFrame({"days":[1,2,3,4,5,6],"stud_name":['a','b','c','a','b','c'],"eng":[10,12,14,15,16,12],"math":[17,18,19,23,34,12]})
var1
var1.pivot(index="days",columns="stud_name",values="eng")

var=pd.DataFrame({"days":[1,1,1,2,2,2],"stud_name":['a','b','c','a','b','c'],"eng":[10,12,14,15,16,12],"math":[17,18,19,23,34,12]})
var
var.pivot_table(index="stud_name",columns="days",aggfunc="mean",margins=True)











































