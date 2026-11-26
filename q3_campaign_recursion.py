# HW10 第3題：遞迴計算個人活動的累計廣告費

# 共同設定：輸入自己的完整學號
student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]
a = int(student_id[-3])
b = int(student_id[-2])
c = int(student_id[-1])
s = a + b + c

# 建立每日廣告費
daily_spend = [
    100 + 10 * a,
    150 + 10 * b,
    0,
    200 + 10 * c,
    50 + 10 * s
]
n = 3 + c % 3

# 定義遞迴函式
def cumulative_spend(daily_spend, n):
    if n == 0:
        return 0

    return cumulative_spend(daily_spend, n - 1) + daily_spend[n - 1]


# 印出指定天數的累計費用
print("學號：", student_id)
print("每日費用：", daily_spend)
print("指定n：", n)
print(f"指定前{n}天累計：{cumulative_spend(daily_spend, n)}元")

# 測試前0至5天
for i in range(6):
    print(f"前{i}天：{cumulative_spend(daily_spend, i)}元")

# 空資料測試
print("空資料：", cumulative_spend([], 0), "元")
