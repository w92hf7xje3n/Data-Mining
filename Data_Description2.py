import pandas as pd
import matplotlib.pyplot as plt

# 讀檔
df = pd.read_csv("StudentsPerformance.csv")

# 散布圖_gender vs math score
gender_male = []
gender_female = []
for i in range(len(df)):
    if df['gender'][i] == "male":
        gender_male.append(df['math score'][i])
        gender_female.append(None)
    else:
        gender_male.append(None)
        gender_female.append(df['math score'][i])

plt.scatter(df['gender'].index, gender_male, label='male', c='b')
plt.scatter(df['gender'].index, gender_female, label='female', c='r')
plt.legend(loc='best')
plt.title('Gender vs Math score')
plt.xlabel('score')
plt.ylabel('numbers of people')
fig = plt.gcf()
fig.savefig('gender_math_score.png', dpi=200)

plt.cla()

# 散布圖_gender vs reading score
gender_male = []
gender_female = []
for i in range(len(df)):
    if df['gender'][i] == "male":
        gender_male.append(df['reading score'][i])
        gender_female.append(None)
    else:
        gender_male.append(None)
        gender_female.append(df['reading score'][i])

plt.scatter(df['gender'].index, gender_male, label='male', c='b')
plt.scatter(df['gender'].index, gender_female, label='female', c='r')
plt.legend(loc='best')
plt.title('Gender vs Reading score')
plt.xlabel('score')
plt.ylabel('numbers of people')
fig = plt.gcf()
fig.savefig('gender_reading_score.png', dpi=200)

plt.cla()

# 散布圖_gender vs writing score
gender_male = []
gender_female = []
for i in range(len(df)):
    if df['gender'][i] == "male":
        gender_male.append(df['writing score'][i])
        gender_female.append(None)
    else:
        gender_male.append(None)
        gender_female.append(df['writing score'][i])

plt.scatter(df['gender'].index, gender_male, label='male', c='b')
plt.scatter(df['gender'].index, gender_female, label='female', c='r')
plt.legend(loc='best')
plt.title('Gender vs Writing score')
plt.xlabel('student index')
plt.ylabel('score')
fig = plt.gcf()
fig.savefig('gender_writing_score.png', dpi=200)

plt.cla()

# -------------------------------------------------------------------------------

group_A = []
group_B = []
group_C = []
group_D = []
group_E = []

for i in range(len(df)):
    if df['race/ethnicity'][i] == "group A":
        group_A.append(df['math score'][i])
        group_B.append(None)
        group_C.append(None)
        group_D.append(None)
        group_E.append(None)
    elif df['race/ethnicity'][i] == "group B":
        group_B.append(df['math score'][i])
        group_A.append(None)
        group_C.append(None)
        group_D.append(None)
        group_E.append(None)
    elif df['race/ethnicity'][i] == "group C":
        group_C.append(df['math score'][i])
        group_A.append(None)
        group_B.append(None)
        group_D.append(None)
        group_E.append(None)
    elif df['race/ethnicity'][i] == "group D":
        group_D.append(df['math score'][i])
        group_A.append(None)
        group_B.append(None)
        group_C.append(None)
        group_E.append(None)
    elif df['race/ethnicity'][i] == "group E":
        group_E.append(df['math score'][i])
        group_A.append(None)
        group_B.append(None)
        group_C.append(None)
        group_D.append(None)

plt.scatter(df['race/ethnicity'].index, group_A, label='group A', alpha=0.7)
plt.scatter(df['race/ethnicity'].index, group_B, label='group B', alpha=0.7)
plt.scatter(df['race/ethnicity'].index, group_C, label='group C', alpha=0.7)
plt.scatter(df['race/ethnicity'].index, group_D, label='group D', alpha=0.7)
plt.scatter(df['race/ethnicity'].index, group_E, label='group E', alpha=0.7)
plt.title('Group vs math score')
plt.xlabel('student index')
plt.ylabel('score')
plt.legend(loc='best')

fig = plt.gcf()
fig.savefig('group_math_score.png', dpi=200)

plt.cla()

# -------------------------------------------------------------------------------

group_A = []
group_B = []
group_C = []
group_D = []
group_E = []

for i in range(len(df)):
    if df['race/ethnicity'][i] == "group A":
        group_A.append(df['reading score'][i])
        group_B.append(None)
        group_C.append(None)
        group_D.append(None)
        group_E.append(None)
    elif df['race/ethnicity'][i] == "group B":
        group_B.append(df['reading score'][i])
        group_A.append(None)
        group_C.append(None)
        group_D.append(None)
        group_E.append(None)
    elif df['race/ethnicity'][i] == "group C":
        group_C.append(df['reading score'][i])
        group_A.append(None)
        group_B.append(None)
        group_D.append(None)
        group_E.append(None)
    elif df['race/ethnicity'][i] == "group D":
        group_D.append(df['reading score'][i])
        group_A.append(None)
        group_B.append(None)
        group_C.append(None)
        group_E.append(None)
    elif df['race/ethnicity'][i] == "group E":
        group_E.append(df['reading score'][i])
        group_A.append(None)
        group_B.append(None)
        group_C.append(None)
        group_D.append(None)

plt.scatter(df['race/ethnicity'].index, group_A, label='group A', alpha=0.7)
plt.scatter(df['race/ethnicity'].index, group_B, label='group B', alpha=0.7)
plt.scatter(df['race/ethnicity'].index, group_C, label='group C', alpha=0.7)
plt.scatter(df['race/ethnicity'].index, group_D, label='group D', alpha=0.7)
plt.scatter(df['race/ethnicity'].index, group_E, label='group E', alpha=0.7)
plt.title('Group vs reading score')
plt.xlabel('student index')
plt.ylabel('score')
plt.legend(loc='best')

fig = plt.gcf()
fig.savefig('group_reading_score.png', dpi=200)

plt.cla()

# -------------------------------------------------------------------------------

group_A = []
group_B = []
group_C = []
group_D = []
group_E = []

for i in range(len(df)):
    if df['race/ethnicity'][i] == "group A":
        group_A.append(df['writing score'][i])
        group_B.append(None)
        group_C.append(None)
        group_D.append(None)
        group_E.append(None)
    elif df['race/ethnicity'][i] == "group B":
        group_B.append(df['writing score'][i])
        group_A.append(None)
        group_C.append(None)
        group_D.append(None)
        group_E.append(None)
    elif df['race/ethnicity'][i] == "group C":
        group_C.append(df['writing score'][i])
        group_A.append(None)
        group_B.append(None)
        group_D.append(None)
        group_E.append(None)
    elif df['race/ethnicity'][i] == "group D":
        group_D.append(df['writing score'][i])
        group_A.append(None)
        group_B.append(None)
        group_C.append(None)
        group_E.append(None)
    elif df['race/ethnicity'][i] == "group E":
        group_E.append(df['writing score'][i])
        group_A.append(None)
        group_B.append(None)
        group_C.append(None)
        group_D.append(None)

plt.scatter(df['race/ethnicity'].index, group_A, label='group A', alpha=0.7)
plt.scatter(df['race/ethnicity'].index, group_B, label='group B', alpha=0.7)
plt.scatter(df['race/ethnicity'].index, group_C, label='group C', alpha=0.7)
plt.scatter(df['race/ethnicity'].index, group_D, label='group D', alpha=0.7)
plt.scatter(df['race/ethnicity'].index, group_E, label='group E', alpha=0.7)
plt.title('Group vs writing score')
plt.xlabel('student index')
plt.ylabel('score')
plt.legend(loc='best')

fig = plt.gcf()
fig.savefig('group_writing_score.png', dpi=200)

plt.cla()

# -------------------------------------------------------------------------------

master = []
bachelor = []
associate = []
college = []
high_school = []
some_high_school = []

for i in range(len(df)):
    if df['parental level of education'][i] == "master's degree":
        master.append(df['math score'][i])
        bachelor.append(None)
        associate.append(None)
        college.append(None)
        high_school.append(None)
        some_high_school.append(None)
    elif df['parental level of education'][i] == "bachelor's degree":
        bachelor.append(df['math score'][i])
        master.append(None)
        associate.append(None)
        college.append(None)
        high_school.append(None)
        some_high_school.append(None)
    elif df['parental level of education'][i] == "associate's degree":
        associate.append(df['math score'][i])
        master.append(None)
        bachelor.append(None)
        college.append(None)
        high_school.append(None)
        some_high_school.append(None)
    elif df['parental level of education'][i] == "some college":
        college.append(df['math score'][i])
        master.append(None)
        bachelor.append(None)
        associate.append(None)
        high_school.append(None)
        some_high_school.append(None)
    elif df['parental level of education'][i] == "high school":
        high_school.append(df['math score'][i])
        master.append(None)
        bachelor.append(None)
        associate.append(None)
        college.append(None)
        some_high_school.append(None)
    elif df['parental level of education'][i] == "some high school":
        some_high_school.append(df['math score'][i])
        master.append(None)
        bachelor.append(None)
        associate.append(None)
        college.append(None)
        high_school.append(None)

plt.scatter(df['parental level of education'].index, master, label="master's degree", alpha=0.7)
plt.scatter(df['parental level of education'].index, bachelor, label="bachelor's degree", alpha=0.7)
plt.scatter(df['parental level of education'].index, associate, label="associate's degree", alpha=0.7)
plt.scatter(df['parental level of education'].index, college, label="some college", alpha=0.7)
plt.scatter(df['parental level of education'].index, high_school, label="high school", alpha=0.7)
plt.scatter(df['parental level of education'].index, some_high_school, label="some high school", alpha=0.7)

plt.title('parental level of education vs math score')
plt.xlabel('student index')
plt.ylabel('score')
plt.legend(loc='best')

fig = plt.gcf()
fig.savefig('parental_level_of_education_math_score.png', dpi=200)

plt.cla()

# -------------------------------------------------------------------------------

master = []
bachelor = []
associate = []
college = []
high_school = []
some_high_school = []

for i in range(len(df)):
    if df['parental level of education'][i] == "master's degree":
        master.append(df['reading score'][i])
        bachelor.append(None)
        associate.append(None)
        college.append(None)
        high_school.append(None)
        some_high_school.append(None)
    elif df['parental level of education'][i] == "bachelor's degree":
        bachelor.append(df['reading score'][i])
        master.append(None)
        associate.append(None)
        college.append(None)
        high_school.append(None)
        some_high_school.append(None)
    elif df['parental level of education'][i] == "associate's degree":
        associate.append(df['reading score'][i])
        master.append(None)
        bachelor.append(None)
        college.append(None)
        high_school.append(None)
        some_high_school.append(None)
    elif df['parental level of education'][i] == "some college":
        college.append(df['reading score'][i])
        master.append(None)
        bachelor.append(None)
        associate.append(None)
        high_school.append(None)
        some_high_school.append(None)
    elif df['parental level of education'][i] == "high school":
        high_school.append(df['reading score'][i])
        master.append(None)
        bachelor.append(None)
        associate.append(None)
        college.append(None)
        some_high_school.append(None)
    elif df['parental level of education'][i] == "some high school":
        some_high_school.append(df['reading score'][i])
        master.append(None)
        bachelor.append(None)
        associate.append(None)
        college.append(None)
        high_school.append(None)

plt.scatter(df['parental level of education'].index, master, label="master's degree", alpha=0.7)
plt.scatter(df['parental level of education'].index, bachelor, label="bachelor's degree", alpha=0.7)
plt.scatter(df['parental level of education'].index, associate, label="associate's degree", alpha=0.7)
plt.scatter(df['parental level of education'].index, college, label="some college", alpha=0.7)
plt.scatter(df['parental level of education'].index, high_school, label="high school", alpha=0.7)
plt.scatter(df['parental level of education'].index, some_high_school, label="some high school", alpha=0.7)

plt.title('parental level of education vs reading score')
plt.xlabel('student index')
plt.ylabel('score')
plt.legend(loc='best')

fig = plt.gcf()
fig.savefig('parental_level_of_education_reading_score.png', dpi=200)

plt.cla()

# -------------------------------------------------------------------------------

master = []
bachelor = []
associate = []
college = []
high_school = []
some_high_school = []

for i in range(len(df)):
    if df['parental level of education'][i] == "master's degree":
        master.append(df['writing score'][i])
        bachelor.append(None)
        associate.append(None)
        college.append(None)
        high_school.append(None)
        some_high_school.append(None)
    elif df['parental level of education'][i] == "bachelor's degree":
        bachelor.append(df['writing score'][i])
        master.append(None)
        associate.append(None)
        college.append(None)
        high_school.append(None)
        some_high_school.append(None)
    elif df['parental level of education'][i] == "associate's degree":
        associate.append(df['writing score'][i])
        master.append(None)
        bachelor.append(None)
        college.append(None)
        high_school.append(None)
        some_high_school.append(None)
    elif df['parental level of education'][i] == "some college":
        college.append(df['writing score'][i])
        master.append(None)
        bachelor.append(None)
        associate.append(None)
        high_school.append(None)
        some_high_school.append(None)
    elif df['parental level of education'][i] == "high school":
        high_school.append(df['writing score'][i])
        master.append(None)
        bachelor.append(None)
        associate.append(None)
        college.append(None)
        some_high_school.append(None)
    elif df['parental level of education'][i] == "some high school":
        some_high_school.append(df['writing score'][i])
        master.append(None)
        bachelor.append(None)
        associate.append(None)
        college.append(None)
        high_school.append(None)

plt.scatter(df['parental level of education'].index, master, label="master's degree", alpha=0.7)
plt.scatter(df['parental level of education'].index, bachelor, label="bachelor's degree", alpha=0.7)
plt.scatter(df['parental level of education'].index, associate, label="associate's degree", alpha=0.7)
plt.scatter(df['parental level of education'].index, college, label="some college", alpha=0.7)
plt.scatter(df['parental level of education'].index, high_school, label="high school", alpha=0.7)
plt.scatter(df['parental level of education'].index, some_high_school, label="some high school", alpha=0.7)

plt.title('parental level of education vs writing score')
plt.xlabel('student index')
plt.ylabel('score')
plt.legend(loc='best')

fig = plt.gcf()
fig.savefig('parental_level_of_education_writing_score.png', dpi=200)

plt.cla()

# -------------------------------------------------------------------------------

standard = []
free_reduced = []

for i in range(len(df)):
    if df['lunch'][i] == "standard":
        standard.append(df['math score'][i])
        free_reduced.append(None)
    elif df['lunch'][i] == "free/reduced":
        free_reduced.append(df['math score'][i])
        standard.append(None)

plt.scatter(df['lunch'].index, standard, label="standard", alpha=0.7)
plt.scatter(df['lunch'].index, free_reduced, label="free/reduced", alpha=0.7)

plt.title('lunch vs math score')
plt.xlabel('student index')
plt.ylabel('score')
plt.legend(loc='best')

fig = plt.gcf()
fig.savefig('lunch_math_score.png', dpi=200)

plt.cla()

# -------------------------------------------------------------------------------

standard = []
free_reduced = []

for i in range(len(df)):
    if df['lunch'][i] == "standard":
        standard.append(df['reading score'][i])
        free_reduced.append(None)
    elif df['lunch'][i] == "free/reduced":
        free_reduced.append(df['reading score'][i])
        standard.append(None)

plt.scatter(df['lunch'].index, standard, label="standard", alpha=0.7)
plt.scatter(df['lunch'].index, free_reduced, label="free/reduced", alpha=0.7)

plt.title('lunch vs reading score')
plt.xlabel('student index')
plt.ylabel('score')
plt.legend(loc='best')

fig = plt.gcf()
fig.savefig('lunch_reading_score.png', dpi=200)

plt.cla()

# -------------------------------------------------------------------------------

standard = []
free_reduced = []

for i in range(len(df)):
    if df['lunch'][i] == "standard":
        standard.append(df['writing score'][i])
        free_reduced.append(None)
    elif df['lunch'][i] == "free/reduced":
        free_reduced.append(df['writing score'][i])
        standard.append(None)

plt.scatter(df['lunch'].index, standard, label="standard", alpha=0.7)
plt.scatter(df['lunch'].index, free_reduced, label="free/reduced", alpha=0.7)

plt.title('lunch vs writing score')
plt.xlabel('student index')
plt.ylabel('score')
plt.legend(loc='best')

fig = plt.gcf()
fig.savefig('lunch_writing_score.png', dpi=200)

plt.cla()

# -------------------------------------------------------------------------------

uncompleted = []
completed = []

for i in range(len(df)):
    if df['test preparation course'][i] == "none":
        uncompleted.append(df['math score'][i])
        completed.append(None)
    elif df['test preparation course'][i] == "completed":
        completed.append(df['math score'][i])
        uncompleted.append(None)

plt.scatter(df['test preparation course'].index, uncompleted, label="none", alpha=0.7)
plt.scatter(df['test preparation course'].index, completed, label="completed", alpha=0.7)

plt.title('test preparation course vs math score')
plt.xlabel('student index')
plt.ylabel('score')
plt.legend(loc='best')

fig = plt.gcf()
fig.savefig('test_preparation_course_math_score.png', dpi=200)

plt.cla()

# -------------------------------------------------------------------------------

uncompleted = []
completed = []

for i in range(len(df)):
    if df['test preparation course'][i] == "none":
        uncompleted.append(df['reading score'][i])
        completed.append(None)
    elif df['test preparation course'][i] == "completed":
        completed.append(df['reading score'][i])
        uncompleted.append(None)

plt.scatter(df['test preparation course'].index, uncompleted, label="none", alpha=0.7)
plt.scatter(df['test preparation course'].index, completed, label="completed", alpha=0.7)

plt.title('test preparation course vs reading score')
plt.xlabel('student index')
plt.ylabel('score')
plt.legend(loc='best')

fig = plt.gcf()
fig.savefig('test_preparation_course_reading_score.png', dpi=200)

plt.cla()

# -------------------------------------------------------------------------------

uncompleted = []
completed = []

for i in range(len(df)):
    if df['test preparation course'][i] == "none":
        uncompleted.append(df['writing score'][i])
        completed.append(None)
    elif df['test preparation course'][i] == "completed":
        completed.append(df['writing score'][i])
        uncompleted.append(None)

plt.scatter(df['test preparation course'].index, uncompleted, label="none", alpha=0.7)
plt.scatter(df['test preparation course'].index, completed, label="completed", alpha=0.7)

plt.title('test preparation course vs writing score')
plt.xlabel('student index')
plt.ylabel('score')
plt.legend(loc='best')

fig = plt.gcf()
fig.savefig('test_preparation_course_writing_score.png', dpi=200)

plt.cla()
