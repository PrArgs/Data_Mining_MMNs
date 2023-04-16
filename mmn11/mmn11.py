import csv
import time
import numpy as np
import pandas as pd 
import os.path
import re

def __is_numeric(data_frame,column_index):
            if (data_frame[column_index].dtype == np.int64 or data_frame[column_index].dtype == np.float64 or data_frame[column_index].dtype == np.int32 or data_frame[column_index].dtype == np.float32):
                return True
            else:
                return False
def __is_string(data_frame,column_index):
    if (data_frame[column_index].dtype == np.object):
        return True
    else:
        return False
def __is_date(data_frame,column_index):
    if (data_frame[column_index].dtype == np.datetime64):
        return True
    else:
        return False
def __is_boolean(data_frame,column_index):
    if (data_frame[column_index].dtype == np.bool):
        return True
    else:
        return False
def __is_categorical(data_frame,column_index):
    if (data_frame[column_index].dtype == np.object):
        return True
    else:
        return False
    
# emporting the data and assign it to be a type data frame

Data = pd.read_csv("mmn11_data.csv" , encoding='utf-8')

#Ready the data to be printed only when needed.
def __print_data(Data):
    pd.options.mode.chained_assignment = None  # default='warn'
    #copy the data frame
    Data = Data.copy()
    #reverse the order of the columns
    #Revers hebrew string in each cell
    for column in Data.columns:
        for i in range(len(Data[column])):
            val = Data[column][i]
            if (type(val) == str) and (re.search(r'[א-ת]+', val)):                
                Data.at[i ,column] = val[::-1]    
    return Data

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
    columns_type = {}
    for column in data_frame.columns:
        if (__is_numeric(data_frame,column) == True):
            columns_type[column] = "numeric"
        elif (__is_string(data_frame,column) == True):
            columns_type[column] = "string"
        elif (__is_date(data_frame,column) == True):
            columns_type[column] = "date"
        elif (__is_boolean(data_frame,column) == True):
            columns_type[column] = "boolean"
        elif (__is_categorical(data_frame,column) == True):
            columns_type[column] = "categorical"
    return columns_type
   

#locating and removing noise values from the data frame if asked
def __noise_cnacletion(data_frame, remove = False):
    # retun not implimented error for now
    raise NotImplementedError("This function is not implemented yet")

def __missing_values_handler(data_frame,column_index,handle = False):
        if (handle == False):
            # turn the column to a list for visualization
            tmp = data_frame[column_index].get_values().tolist()
            print("\n this is the missing values in columns: \n ]")
            print(tmp)
            time.sleep(1)
            #ask the udser if he wants to handle the missing values yes/no
            ans = input("Do you want to handle the missing values? (yes/no) ")
            if (ans == "yes"):
                #offers a menu to the user to choose how to handle the missing values by column type
                #and uses switch case by user's choice to handle the missing 

                if (__is_numeric(data_frame,column_index) == True):
                    
                    print("How do you want to handle the missing values? \n")
                    print("enter 1 to replace the missing values with the mean of the column \n")
                    print("enter 2 to replace the missing values with the median of the column \n")
                    print("enter 3 to replace the missing values by findig the most common value in the column \n")
                    print("enter 4 to replace the missing values by inding association rules between columns \n")
                    print("enter 5 to replace the missing values by finding the most similar row \n")
                    print("enter 6 to replace the missing values by a default value \n")
                    print("enter 7 to add row to the data frame by the frequency of the missing values \n")
                    ans = input("enter your choice: ")
                    if (ans == "1"):
                        data_frame[column_index] = data_frame[column_index].fillna(data_frame[column_index].mean())
                    elif (ans == "2"):
                        data_frame[column_index] = data_frame[column_index].fillna(data_frame[column_index].median())
                    elif (ans == "3"):
                        #find the most common value in the column
                        most_common_value = data_frame[column_index].value_counts().idxmax()
                        data_frame[column_index] = data_frame[column_index].fillna(most_common_value)
                    elif (ans == "4"):
                        #find association rules between columns
                        print("sorry not supported yet")
                    elif (ans == "5"):
                        #find the most similar row
                        print("sorry not supported yet")
                    elif (ans == "6"):
                        #replace the missing values by a default value
                        default_value = input("enter the default value: ")
                        data_frame[column_index] = data_frame[column_index].fillna(default_value)
                    elif (ans == "7"):
                        #add row to the data frame by the frequency of the missing values
                        print("sorry not supported yet")
        else:
            print ("please make shure that the missing values are handled \n")

#locating and handling missing values from the data frame if asked
def __missing_values_cnacletion(data_frame, handle = False):
    # retun not implimented error for now
    types = __find_type_of_columns(data_frame)
    #find the missing values and corrupt values in each column and save the column's index in a list
    
    #Check if frame containes symbols using regex and turn them to NaN
    for column in data_frame.columns:
        for i in range(len(data_frame[column])):
            val = data_frame.iloc[i][column]
            if (type(val) == str) and (re.search(r'[?]+', val)):
                data_frame.at[i,column] = np.nan
    
    
    missing_values = []    
    for column in data_frame.columns:
        #save the the colum to the list if it contains missing values or NAN
        if (data_frame[column].isnull().any() == True):
            missing_values.append(data_frame[column])
    #print the missing values
    print("\n this is the missing values: \n")
    print(missing_values)
    time.sleep(2)
    
        
        
    
    #if there are missing values or corrupt values in the data frame ask the user if he wants to handle them
    # or handle them automaticly
    for colummn in missing_values:        
        __missing_values_handler(data_frame, missing_values, handle)
    else:
        print("\n There are no missing values in the data frame \n")
        time.sleep(2)

        
    

    

        
        
    
    #consolt about best way to handle missing values in specific column




    
        
            
            
    #print the missing values
    print("\n this is the missing values: \n")
    time.sleep(2)
    for column in missing_values:
        print(missing_values[column])
    

#locating and handling ubnormal values from the data frame if asked
def __ubnormal_values_cnacletion(data_frame, remove = False):
    # retun not implimented error for now
    raise NotImplementedError("This function is not implemented yet")

#Aplly all the cleaning functions on a data frame:
def clean_data(data_frame, remove = False):
    #Print the data 
    print("\n this is the initial data frame: \n")
    print(__print_data(Data))
    time.sleep(2)
    __handle_duplicated_rows(data_frame, remove)
    #__noise_cnacletion(data_frame, remove)    
    __missing_values_cnacletion(data_frame, remove)

#Clean the data and show the process
clean_data(Data, False)

    

#Finding association rules between columns











