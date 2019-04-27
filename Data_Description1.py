import pandas as pd
import matplotlib.pyplot as plt

# 讀檔
df = pd.read_csv("StudentsPerformance.csv")

# 檢視檔案有多少筆資料
print('資料筆數:' + str(df.shape))
print('------------------------------------------------------------------------')

# 檢視資料長相
print('資料長相:\n' + str(df.head()))
print('------------------------------------------------------------------------')

# 檢視資料欄位名稱
print('資料欄位名稱:')
print(df.columns)
print('------------------------------------------------------------------------')

# 檢視資料索引
print('資料索引:')
print(df.index)
print('------------------------------------------------------------------------')

# 檢視資料各欄位訊息
print('資料欄位資訊:')
print(df.info())
print('------------------------------------------------------------------------')

# 檢查資料是否有缺值NaN
print('檔案是否有缺值:' + str(df.isnull().values.any()))
print('------------------------------------------------------------------------')

# 檢視資料基本統計值
print('資料基本統計數值:')
print(df.describe())

# -------------------------------------------------------------------------------
# math score直方圖
plt.hist(df['math score'], bins=20, alpha=0.3, label='math', edgecolor='b')

# reading score直方圖
plt.hist(df['reading score'], bins=20, alpha=0.3, label='reading', edgecolor='r')

# writing score直方圖
plt.hist(df['writing score'], bins=20, alpha=0.3, label='writing', edgecolor='g')

# save score figure
plt.title('score')
plt.xlabel('score')
plt.ylabel('numbers of people')
plt.legend(loc='upper right')
fig = plt.gcf()
fig.savefig('score_hist.png', dpi=100)
# -------------------------------------------------------------------------------
