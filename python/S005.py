#%%
import pdfplumber
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 中文字形
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']   
plt.rcParams['axes.unicode_minus'] = False


# 輸入要查詢的名字
allName = [input(f'請輸入要查詢人名{i+1}：') for i in range(3)]

# 初始化計數
allSum = [0] * 3

# 開啟 PDF 並計算出現次數
with pdfplumber.open('T004.pdf') as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            for i in range(3):
                allSum[i] += text.count(allName[i])

# 顯示統計結果
for i in range(3):
    print(f"{allName[i]} 共出現 {allSum[i]} 次")

# 繪製長條圖
x = np.arange(len(allName))
plt.bar(x, allSum, color=['red', 'green', 'blue'])
plt.xticks(x, allName)
plt.xlabel('Name')
plt.ylabel('Count')
plt.title('名字出現次數')
plt.show()

# %%
