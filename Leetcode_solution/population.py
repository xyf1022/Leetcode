import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为SimHei
# 定义文件名
filename = '人口.txt'

# 打开文件并读取内容
with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 修改每一行，添加双引号
quoted_lines = [f'"{line.strip()}"\n' for line in lines]

# 打印结果（如果你想写回文件，可以取消注释以下两行）
with open('quoted_' + filename, 'w', encoding='utf-8') as file:
    file.writelines(quoted_lines)

# 打印到控制台
for quoted_line in quoted_lines:
    print(quoted_line, end='')  # 使用end=''来避免打印额外的换行符

# 提取年份后的数据
extracted_data = []
for item in quoted_lines:
    # 去除字符串两端的引号，并检查字符串是否为空
    stripped_item = item.strip('"')
    if stripped_item:  # 如果字符串不为空
        # 分割字符串，获取年份后面的部分
        year_and_value = stripped_item.split("：")
        if len(year_and_value) == 2:
            # 提取并存储数据部分（这里我们假设数据部分总是以“万”结尾，但你可以根据需要处理）
            value_with_unit = year_and_value[1]
            extracted_data.append(value_with_unit)

        # 打印提取的数据
print(extracted_data)

# 处理每个字符串，去除"万"和换行符
cleaned_data = []
for item in extracted_data:
    # 先去除换行符，再去除"万"
    cleaned_item = int(item.replace('\n', '').replace('万', '').replace('"','').replace(',',''))
    cleaned_data.append(cleaned_item)

# 打印处理后的数据
print(cleaned_data)
years = np.arange(1929, 2023)
print(years)

# 绘制折线图
plt.plot(years, cleaned_data, marker='o')  # 使用圆圈标记数据点

# 添加标题和标签
plt.title('年份与人口的折线图')
plt.xlabel('年份')
plt.ylabel('人口（万）')

# 显示网格线
plt.grid(True)

# 显示图表
plt.show()

