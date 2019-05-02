from apyori import apriori
import pandas as pd

# 讀檔
df = pd.read_csv("StudentsPerformance.csv")

# 資料替換
# A1=male, A2=female
df.replace(['male', 'female'], ['A1', 'A2'], inplace=True)
# B1=group A, B2=group B, B3=group C, B4=group D, B5=group E
df.replace(['group A', 'group B', 'group C', 'group D', 'group E'], ['B1', 'B2', 'B3', 'B4', 'B5'], inplace=True)
# C1=master's degree, C2=bachelor's degree, C3=associate's degree, C4=some college, C5=high school, C6=some high school
df.replace(["master's degree", "bachelor's degree", "associate's degree", "some college", "high school", "some high "
                                                                                                         "school"],
           ["C1", "C2", "C3", "C4", "C5", "C6"], inplace=True)
# D1=standard, D2=free/reduced
df.replace(['standard', 'free/reduced'], ['D1', 'D2'], inplace=True)
# E1=none, E2=completed
df.replace(['none', 'completed'], ['E1', 'E2'], inplace=True)

# 建一二維列表for math grade >= 60
df_math_score = df.values.tolist()
df_math_score = [x for x in df_math_score if x[5] >= 60]
for i in df_math_score:
    del i[5]
    del i[5]
    del i[5]

# 建一二維列表for reading grade >= 60
df_reading_score = df.values.tolist()
df_reading_score = [x for x in df_reading_score if x[6] >= 60]
for i in df_reading_score:
    del i[5]
    del i[5]
    del i[5]

# 建一個二維列表for writing grade >= 60
df_writing_score = df.values.tolist()
df_writing_score = [x for x in df_writing_score if x[7] >= 60]
for i in df_writing_score:
    del i[5]
    del i[5]
    del i[5]

association_results_math = list(apriori(df_math_score, min_support=0.2))
# print(association_results_math)
association_results_reading = list(apriori(df_reading_score, min_support=0.2))
# print(association_results_reading)
association_results_writing = list(apriori(df_writing_score, min_support=0.2))
# print(association_results_writing)

# 顯示出math score > 60 的 frequent item_set 跟 support
print('\n=========================== math score ==============================')
for item in association_results_math:
    print('frequent item_set: ' + str(item[0]) + ' support: ' + str(item[1]))

# 顯示出reading score > 60 的 frequent item_set 跟 support
print('\n=========================== reading score ==============================')
for item in association_results_reading:
    print('frequent item_set: ' + str(item[0]) + ' support: ' + str(item[1]))

# 顯示出writing score > 60 的 frequent item_set 跟 support
print('\n=========================== writing score ==============================')
for item in association_results_writing:
    print('frequent item_set: ' + str(item[0]) + ' support: ' + str(item[1]))
