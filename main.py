#-----------CHECK EXISTENCE OF A NUMBER FROM TWO FILES------

# with open("file1.txt") as f:
#     file1List = [int(line.strip()) for line in f]
# print(file1List)
# with open("file2.txt") as f:
#     file2List = [int(line.strip()) for line in f]
# print(file2List)
# # file1List=file1List+(file2List)
# # print(file1List)
# result=[ n for n in file1List if n in file2List]
#
# # Write your code above 👆
# print(result)

#----------------FILTER EVEN NUMBERS---------
# list1=input().split(",")
# list1=["1","2","3","4","5"]
# int_result=[int(n) for n in list1]
# # print(int_result)
# result=[n for n in int_result if n%2==0]
# print(result)

#---------------DICTIONARY COMPREHENSIONS--------

# import random
# name=["name1","name2","name3","name4"]
# score_dict={i:random.randint(10,100) for i in name }
# print(score_dict)
# pass_score_dict={i:j for (i,j) in score_dict.items() if j>60}
# print(pass_score_dict)

#---------------SENTENCE TO DICTIONARY--
# sentence="What is the Airspeed Velocity of an Unladen Swallow?"
# sentence1=sentence.split(" ")
# # print(sentence1)
# dict_sizes_of_words={key:len(key) for (key) in sentence1}
# print(dict_sizes_of_words)

#-------------TEMP CHANGING PROJECT(CELSIUS TO FARENHEIT DICTIOARY CONVERSION)---------------
# weather_c={"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f={key:(value*9/5)+32 for (key,value) in weather_c.items()}
# print(weather_f)

#-------------ITERATE OVER PANDAS DATAFRAME---------
student_dict={
    "student":["Angela","James","Lily"],
    "score":[56,76,88]
}

# for (key,value) in  student_dict.items():
#     print(key, value)   #     student ['Angela', 'James', 'Lily']
                        # score [56, 76, 88]

import pandas
df=pandas.DataFrame(student_dict)
# print(df) #   student  score
            # 0  Angela     56
            # 1   James     76
            # 2    Lily     88
# for (key,value) in df.items():
#     print(key)  # student
#                 # 0    Angela
#                 # 1     James
#                 # 2      Lily
#
#     print(value)    # score
#                     # 0    56
#                     # 1    76
#                     # 2    88
#----this is looping over columns. and creating weird dictionary----
# new_dict={key:value for (key,value) in df.items()}
# print(new_dict)
#---to loop over the rows, we have iterrows in pandas
#------- to iterate over rows using the indices------

for (index,row) in df.iterrows():
    print(index)  # 0
                    # 1
                    # 2
    #-----------------
    # print(row.student)
# Angela
# James
# Lily
    # -----------------
    # print(row.score)
# 56
# 76
# 88
    # -----------------
    # print(row)
# student    Angela
# score          56
# Name: 0, dtype: object
# student    James
# score         76
# Name: 1, dtype: object
# student    Lily
# score        88
# Name: 2, dtype: object


