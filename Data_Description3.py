import pandas as pd
import matplotlib.pyplot as plt

# 讀檔
df = pd.read_csv("StudentsPerformance.csv")

# for 相關係數的dataframe
dataframe = pd.DataFrame()
dataframe['math score'] = df['math score']
dataframe['reading score'] = df['reading score']
dataframe['writing score'] = df['writing score']

print(dataframe.corr())

plt.scatter(dataframe['math score'], dataframe['reading score'], alpha=0.7)
plt.title('math score vs reading score')
plt.xlabel('math score')
plt.ylabel('reading score')
fig = plt.gcf()
fig.savefig('corr_math_reading', dpi=200)

plt.cla()

# -------------------------------------------------------------------------

plt.scatter(dataframe['math score'], dataframe['writing score'], alpha=0.7)
plt.title('math score vs writing score')
plt.xlabel('math score')
plt.ylabel('writing score')
fig = plt.gcf()
fig.savefig('corr_math_writing', dpi=200)

plt.cla()

# -------------------------------------------------------------------------

plt.scatter(dataframe['reading score'], dataframe['writing score'], alpha=0.7)
plt.title('reading score vs writing score')
plt.xlabel('reading score')
plt.ylabel('writing score')
fig = plt.gcf()
fig.savefig('corr_reading_writing', dpi=200)

plt.cla()
