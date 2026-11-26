# HW10 第4題：清理素材點擊資料並產生排名

# 共同設定：輸入自己的完整學號
student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]
a = int(student_id[-3])
b = int(student_id[-2])
c = int(student_id[-1])
s = a + b + c

# 建立素材點擊資料
raw_clicks = [
    str(10 + a),
    "0",
    "",
    " " + str(5 + b) + " ",
    "   ",
    str(15 + c),
    str(5 + b)
]
min_clicks = 5 + b

# 定義資料清理與篩選函式
def select_clicks(raw_clicks, min_clicks=10):
    cleaned = map(lambda x: x.strip(), raw_clicks)
    valid = filter(None, cleaned)
    numbers = list(map(int, valid))

    qualified = list(
        filter(lambda x: x >= min_clicks, numbers)
    )

    return numbers, qualified


# 使用個人點擊門檻
numbers, qualified = select_clicks(
    raw_clicks,
    min_clicks=min_clicks
)

print("學號：", student_id)
print("點擊門檻：", min_clicks)
print("清理結果：", numbers)
print("合格結果：", qualified)
print("合格筆數：", len(qualified))
print("合格合計：", sum(qualified))

# 由大到小排名；相同點擊數仍分別列出
ranking = sorted(qualified, reverse=True)
for rank, clicks in enumerate(ranking, start=1):
    print(f"第{rank}名：{clicks}次")

# 使用同一份原始資料測試門檻100
numbers_100, qualified_100 = select_clicks(
    raw_clicks,
    min_clicks=100
)

print("門檻100合格結果：", qualified_100)
print("門檻100合格筆數：", len(qualified_100))
print("門檻100合格合計：", sum(qualified_100))

if len(qualified_100) == 0:
    print("無符合門檻的素材")
