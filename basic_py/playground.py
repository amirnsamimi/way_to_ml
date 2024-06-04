#my playground for py to learn 

typeCheck = type("Amir's Playground") 

multiply = 2*2
division = 2/2
modulo = 2%4
power = 2**3
subtraction = 2-2
addition = 2+2

to_str = str(2) 
to_int = int("2")
to_float = float("2.23")   
to_boolean = bool(1) 

str_concatination = "Hello" + "World"
str_Muliplying = "Hello" * 3

list_sample = ["amir","samimi",29,"verheiratet"]
subseting_list = list_sample[-1]
subseting_list_2 = list_sample[2]
copying_lists = list_sample[:]
copying_lists_2 = list(list_sample)

#changing list indexes values
list_sample[2] = 30
 
defining_variables = "Hello"
#changing variables & copying respectively 
defining_variables = "bye"
copy_of_var = defining_variables
capitalizing_first_letter = defining_variables.capitalize()
uppercasing_string = defining_variables.upper()
counting_string_length = defining_variables.count("l")
replacing_in_str = defining_variables.replace("l","y")

list_sample_2 = [1,2,4,5,7,12,3,2,54,6,12,42,34,53,23,67,6,43,23,4,1,23,4,3,6,7,8,0,-100,9]
max_of_list = max(list_sample_2)
min_of_list = min(list_sample_2)
len_of_list = len(list_sample_2)
index_of_item = list_sample_2.index(54)
remove_an_intem = list_sample_2.remove(6)
reversed_list = list_sample_2.reverse()
appending_to_list = list_sample_2.append(21245)
counting_list_item = list_sample_2.count(6)

#deleting an index from an array
del(list_sample_2[-3])

#help on built-in methods and funcs 
#help will print always so I comment it
#help(max)

list_of_lists = [copying_lists,list_sample_2]
subseting_list_of_lists = list_of_lists[0][1:3]

appending_lists = copying_lists + list_sample_2



float_sample = 3.1452423424242
rounding_samlpe = round(float_sample,2) #3
sorting_lists = sorted(list_sample_2,reverse=True)


#comparision operators
float_sample_2 = 5.24
greater_than = float_sample_2 > float_sample
smaller_than = float_sample_2 < float_sample
equal_to = float_sample_2 == float_sample
not_equal_to = float_sample_2 != float_sample
greater_than_or_equal_to = float_sample_2 >= float_sample
smaller_than_or_equal_to = float_sample_2 <= float_sample


#dictionaries
dictionary_sample = {
    "name":"Amir",
    "age": 29
}

subseting_dicts = dictionary_sample["name"]
finding_if_its_valid = "name" in dictionary_sample
del(dictionary_sample["age"])


#pip3 install numpy 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#numpy
#in numpy you can do math on array elements while you cannot do it in py
np_array = np.array([list_sample_2]) 
np_multiplying_array_items = np_array*2

np_subsetting_data_with_comparision_operators = np_array[np_array < 3] 
np_array_shapes = np_array.shape
np_column_stacking = np.column_stack(([1,6],[2,5]))

np_mean = np.mean(np_array)
np_median = np.median(np_array)
np_standard_deviation = np.std(np_array)
np_correlation_coefficient = np.corrcoef(np_array)

np_create_random_number = np.random.normal(4,0.4,1000) #mean std samples
np_create_random_float = np.random.default_rng(124) #ex: seed = 25
np_create_random_float_sample = np_create_random_float.random((3,5))  #ex: 6


#matplotlib

plt_list_year_sample = [1995,2000,2005,2010,2015,2020,2025]
plt_list_data_sample = [3.5124,5.324,2.243,55.623,5.23,22.412,0]

#cause of creation / commented
#plt.scatter(plt_list_year_sample,plt_list_data_sample) # x , y
#plt.show()

#cause of creation / commented
# plt.hist(plt_list_data_sample,bins=2)
# plt.show()

# plt.plot(plt_list_data_sample,plt_list_year_sample)
# plt.xlabel("rain")
# plt.ylabel("year")
# plt.title("raining in year")
# plt.yticks([1995,2025],["first","last"],rotation=45) #for naming for example months of year instead of numbers

# plt.show()


#pandas

import pandas as pd

dictionary_sample_2 = {
    "Rashin-squad": [
      {
        "age": "29",
        "f_name": "Amir",
      },
         {
        "age": "29",
        "f_name": "Rashin",
      },
    ],
    "yasi-squad": [
      {
        "age": "29",
        "f_name": "Soroush",
      },
           {
        "age": "27",
        "f_name": "Yasi",
      },
    ],
}
    
list_sample_3 = [
      {
        "age": "29",
        "f_name": "Amir",
      },
         {
        "age": "29",
        "f_name": "Rashin",
      },
    
      {
        "age": "29",
        "f_name": "Soroush",
      },
           {
        "age": "27",
        "f_name": "Yasi",
      }
]


#one way to get directories instead of "./Investigating_Netflix_movies/netflix_data.csv"
import os
current_directory = os.getcwd()
Investigating_Netflix_movies_directory = os.path.join(current_directory,'.','Investigating_Netflix_movies')
Investigating_Netflix_movies_directory = os.path.abspath(Investigating_Netflix_movies_directory)
netflix_csv_path = os.path.join(Investigating_Netflix_movies_directory,'netflix_data.csv')




pd_data_frame_sample = pd.DataFrame(dictionary_sample_2)
pd_data_frame_sample_2 = pd.DataFrame(list_sample_3) 
pd_data_frame_sample.index = ["user_1_data","user_2_data"] #for each index we can add a name
pd_df_from_CSV = pd.read_csv(netflix_csv_path,index_col=0) #show_id

pd_data_subseting = pd_df_from_CSV["type"] #getting a column all rows as a array
pd_multi_data_subseting = pd_df_from_CSV[["type","genre"]] #getting 2 columns as df
pd_series_type = type(pd_data_subseting) 
pd_df_type = type(pd_multi_data_subseting)
pd_row_subsetting = pd_df_from_CSV[1:12] #getting rows from 1 to 12 
pd_loc_subseting = pd_df_from_CSV.loc[["s3","s5"]] #getting s3 & s5 rows
pd_loc_subseting_2 = pd_df_from_CSV.loc[:,["type"]] #getting all rows of column type
pd_iloc_subseting = pd_df_from_CSV.iloc[[1]] #getting 1 & 4 indexes rows
pd_iloc_subseting_2 = pd_df_from_CSV.iloc[:,[2]] #getting all rows of column index 2


