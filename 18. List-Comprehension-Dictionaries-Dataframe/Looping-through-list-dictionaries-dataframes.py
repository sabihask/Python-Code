student_dict = {
    "student":["sabiha", "Nithya", "Divya"],
    "score":[56, 66, 76]
    }
# #LOOOPING THROUGH DICTIONARY
for (key, value) in student_dict.items():
    print(key)
     print(value)


#LOOPING THROUGH DATAFRAMES

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
#
for (key,value) in student_data_frame.items():
    print(key)
    # print(value)

#LOOP THROUGH ROWS OF A DATAFRAME

for (index,row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    print(row.student)
    print(row.score)
    if(row.student == 'sabiha'):
        print(row.score)
