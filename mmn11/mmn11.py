import csv
import numpy as np
import pandas as pd 
import os.path
    
# making data frame
print("this is the data frame: ")
Data = pd.read_csv("mmn11_data.csv" , encoding='utf-8')


#reverse the order of the columns
Data = Data.reindex(columns=Data.columns[::-1])

#Revers hebrew string in each cell
def reverseString(Data):
    for column in Data.columns:
        for i in range(len(Data[column])):
            if type(Data[column][i]) == str:
                tmp = Data[column][i][::-1]
                Data[column][i] = tmp
    return Data
    
Data = reverseString(Data)
print(Data)


# def mergeTwiceId (Data):
#     dict = {}
#     list =[]
#     #counts how many times ID is in table 
#     for i in Data['ID']:
#         if (i in dict):
#             dict[i] += 1 
#         else:
#             dict[i] = 1
        
#     #returns a list of the IDs reapiting only twice
#     for key, value in dict.items():
#         if value == 2:
#             list.append(key)
#     #make a copy of the data frame on the desktop directory
#     Data_copy = Data.copy()
#     print(pd.read_csv(Data_copy))



#     #merges the data frame with the list of IDs
#     Data_copy.to_csv(os.path.join("C:\\Users\\argam\\Desktop", 'result.csv'))

#     print(pd.read_csv("C:\\Users\\argam\\Desktop\\result.csv"))

#     return None

