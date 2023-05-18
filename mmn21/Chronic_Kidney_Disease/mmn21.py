#this is mmn 21 by Roi Argaman
#this is a Data mining project
# for practice and learning reasons we will try to use functional programming principles

import pandas as pd
import numpy as np
import os

#Assigment the 2 dataframes
path = os.getcwd()
CKD = pd.read_csv('chronic_kidney_disease.csv')
CKD_full = pd.read_csv('chronic_kidney_disease_full.csv')

#print both dataframes
print(CKD)
print(CKD_full)
