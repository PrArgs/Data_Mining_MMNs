import csv
import numpy as np
import pandas as pd 
import os.path
import re
    
# emporting the data and assign it to be a type data frame

Data = pd.read_csv("mmn11_data.csv" , encoding='utf-8')

#Ready the data to be printed only when needed.
def __print_data(Data):
    #copy the data frame
    Data = Data.copy()
    #reverse the order of the columns
    Data = Data.reindex(columns=Data.columns[::-1])
    #Revers hebrew string in each cell
    for column in Data.columns:
        for i in range(len(Data[column])):
            val = Data[column][i]
            if (type(val) == str) and (re.search(r'[א-ת]+', val)):
                tmp = val[::-1]                
                Data[column][i] = tmp
    return Data

#Print the data 
print("\n this is the initial data frame: \n")
print(__print_data(Data))


#Clean the data and reduce the dimentionality of the data frame

#locate duplicated rows and remove them if asked 
def __handle_duplicated_rows(data_frame, remove = False):
    if (data_frame.duplicated().any() == True):
        print("\n this is the duplicated rows: \n")
        print(data_frame[data_frame.duplicated()])

        if (remove == False):
            #ask the udser if he wants to remove the duplicated rows yes/no
            ans = input("Do you want to remove the duplicated rows? (yes/no) ")
            if (ans == "yes"):
                data_frame = data_frame.drop_duplicates()
                print("\n this is the data frame after removing the duplicated rows: \n")
                print(__print_data(data_frame))
        else:
            data_frame = data_frame.drop_duplicates()
    else:
        print("\n There are no duplicated rows in the data frame \n")
            
#finding the type of each column and save it in a dictionary
def __find_type_of_columns(data_frame):
    #create a dictionary to save the type of each column
    types = {}
    for column in data_frame.columns:
        types[column] = type(data_frame[column][0])
    print(types)
    return types

#locating and removing noise values from the data frame if asked
def __noise_cnacletion(data_frame, remove = False):
    # retun not implimented error for now
    raise NotImplementedError("This function is not implemented yet")

#locating and handling missing values from the data frame if asked
def __missing_values_cnacletion(data_frame, remove = False):
    # retun not implimented error for now
    types = __find_type_of_columns(data_frame)
    raise NotImplementedError("This function is not implemented yet")

#locating and handling ubnormal values from the data frame if asked
def __ubnormal_values_cnacletion(data_frame, remove = False):
    # retun not implimented error for now
    raise NotImplementedError("This function is not implemented yet")

#Aplly all the cleaning functions on a data frame:
def clean_data(data_frame, remove = False):
    __handle_duplicated_rows(data_frame, remove)
    __noise_cnacletion(data_frame, remove)
    __missing_values_cnacletion(data_frame, remove)

    

#Finding association rules between columns











