# HW10 第2題：整理兩場電子報活動的個人優惠碼

# 共同設定：輸入自己的完整學號
student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]
a = int(student_id[-3])
b = int(student_id[-2])
c = int(student_id[-1])
s = a + b + c

# 建立優惠碼資料
saved = ["BASE"]
raw_a = [
    " welcome" + tail + " ",
    "vip" + tail,
    "",
    "WELCOME" + tail,
    "   "
]
raw_b = [
    " new" + tail + " ",
    " welcome" + tail + " "
]

# 定義優惠碼整理函式
def collect_codes(raw_codes, saved=None):
    if saved is None:
        result = []
    else:
        result = saved.copy()

    for code in raw_codes:
        code = code.strip().upper()

        if code != "" and code not in result:
            result.append(code)

    return result


# 分別整理兩場活動
activity_a = collect_codes(raw_a, saved=saved)
activity_b = collect_codes(raw_b)

# 印出結果
print("學號：", student_id)
print("活動A：", activity_a)
print("活動B：", activity_b)
print("原始saved：", saved)
print("原始raw_a：", raw_a)

# 空資料測試
print("空資料：", collect_codes([]))
