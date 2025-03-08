import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib.ticker import FormatStrFormatter  # 用于设置 Y 轴坐标格式

# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据（从 Excel 文件中提取，Y 值已放大 10,000 倍）
data = pd.DataFrame({
    -2: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    -1: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    0: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    1: [-2.62626, -3.15914, -3.17243, -2.69731, -1.1854, -1.37587, -1.3846, -1.20721, -0.521982, -0.571674, -0.574213, -0.52917, -0.26403, -0.281285, -0.282509, -0.267606, -0.138732, -0.145985, -0.146691, -0.140836],
    2: [-0.01824, -0.0173049, -0.0176419, -0.0177405, -0.218337, -0.264123, -0.26512, -0.224976, -0.100751, -0.118485, -0.119085, -0.102724, -0.0428656, -0.0472383, -0.0474552, -0.0434624, -0.0211002, -0.0225594, -0.0226556, -0.0213781],
    3: [0.0485797, 0.0622686, 0.0626215, 0.0501995, 0.00666654, 0.0117901, 0.0118086, 0.00784686, -0.207426, -0.251696, -0.253081, -0.213677, -0.0967413, -0.114384, -0.11502, -0.098593, -0.0398305, -0.0441087, -0.0443131, -0.0403818],
    4: [0.0718393, 0.0868718, 0.0872928, 0.073662, 0.072771, 0.0902069, 0.090675, 0.0748724, 0.019642, 0.0263167, 0.0263594, 0.0209218, -0.200301, -0.244262, -0.245496, -0.206573, -0.0938617, -0.111863, -0.112469, -0.0957805],
    5: [0.0846226, 0.100354, 0.100825, 0.0865941, 0.0964947, 0.115296, 0.115861, 0.0988245, 0.0845541, 0.102978, 0.103587, 0.086778, 0.0284403, 0.0358811, 0.0360098, 0.0298268, -0.19446, -0.237607, -0.238914, -0.200384],
    6: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    7: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    8: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    9: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    10: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}, index=range(1, 21))

# 侧边栏
with st.sidebar:
    st.header("标测电极")
    
    # 标测电极A
    electrode_a = st.slider("标测电极A", 1, 20, 10, 1, key="electrode_a")
    
    # 标测电极B
    electrode_b = st.slider("标测电极B", 1, 20, 10, 1, key="electrode_b")
    
    # 调整 X 轴紧凑度的滑动条
    x_spacing = st.slider(
        "X 轴紧凑度", 
        min_value=0.1, 
        max_value=1.0, 
        value=0.5, 
        step=0.1, 
        key="x_spacing"
    )
    
    # 显示具体数值的按钮
    show_values = st.button("显示具体数值")

# 计算差值
diff_a = data.loc[electrode_a]
diff_b = data.loc[electrode_b]
diff_ab = diff_a - diff_b

# 时间序列图
st.header("时间序列图 (Y 值已放大 10,000 倍)")

# 动态调整图像宽度
fig_width = 10 * x_spacing  # 根据 x_spacing 动态调整图像宽度
fig, (ax_a, ax_b, ax_ab) = plt.subplots(3, 1, figsize=(fig_width, 10))

# 动态调整 X 轴范围
x_values = np.arange(len(data.columns)) * x_spacing  # 根据 x_spacing 调整 X 轴范围

# 电极 A
ax_a.plot(x_values, diff_a, marker="o", markersize=4, linewidth=1.5)
ax_a.set_title(f"标测电极A时间序列图（电极 {electrode_a}）", fontsize=10)
ax_a.set_xlabel("时间点", fontsize=8)
ax_a.set_ylabel("")  # 隐藏 Y 轴标签
ax_a.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))  # Y 轴保留两位小数
ax_a.set_xticks(x_values)  # 设置 X 轴刻度
ax_a.set_xticklabels(data.columns, rotation=90, fontsize=8)  # X 轴标签垂直显示
ax_a.grid(True, linestyle="--", alpha=0.6)

# 电极 B
ax_b.plot(x_values, diff_b, marker="o", markersize=4, linewidth=1.5)
ax_b.set_title(f"标测电极B时间序列图（电极 {electrode_b}）", fontsize=10)
ax_b.set_xlabel("时间点", fontsize=8)
ax_b.set_ylabel("")  # 隐藏 Y 轴标签
ax_b.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))  # Y 轴保留两位小数
ax_b.set_xticks(x_values)  # 设置 X 轴刻度
ax_b.set_xticklabels(data.columns, rotation=90, fontsize=8)  # X 轴标签垂直显示
ax_b.grid(True, linestyle="--", alpha=0.6)

# 电极 A-B
ax_ab.plot(x_values, diff_ab, marker="o", markersize=4, linewidth=1.5)
ax_ab.set_title(f"标测电极A-B时间序列图（电极 {electrode_a} - 电极 {electrode_b}）", fontsize=10)
ax_ab.set_xlabel("时间点", fontsize=8)
ax_ab.set_ylabel("")  # 隐藏 Y 轴标签
ax_ab.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))  # Y 轴保留两位小数
ax_ab.set_xticks(x_values)  # 设置 X 轴刻度
ax_ab.set_xticklabels(data.columns, rotation=90, fontsize=8)  # X 轴标签垂直显示
ax_ab.grid(True, linestyle="--", alpha=0.6)

# 调整子图间距
plt.tight_layout()

# 显示图表
st.pyplot(fig)

# 显示具体数值（横排显示）
if show_values:
    st.subheader("具体数值（横排显示）")
    
    # 将数据转换为横排格式
    df_a = pd.DataFrame({f"电极 {electrode_a} ": diff_a}).T
    df_b = pd.DataFrame({f"电极 {electrode_b} ": diff_b}).T
    df_ab = pd.DataFrame({f"电极 {electrode_a} - 电极 {electrode_b} 差值": diff_ab}).T
    
    # 显示表格
    st.write("电极 A：")
    st.dataframe(df_a)
    
    st.write("电极 B ：")
    st.dataframe(df_b)
    
    st.write("电极 A-B 差值：")
    st.dataframe(df_ab)