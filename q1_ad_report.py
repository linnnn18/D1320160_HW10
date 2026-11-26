# HW10 第1題：製作自己的廣告成效報表

# 共同設定：輸入自己的完整學號
student_id = input("請輸入完整學號：").strip().upper()
tail = student_id[-3:]
a = int(student_id[-3])
b = int(student_id[-2])
c = int(student_id[-1])
s = a + b + c

# 建立廣告資料
ads = [
    ("搜尋廣告", 1000 + 100 * a, 30 + 5 * b),
    ("社群廣告", 1200 + 100 * b, 24 + 4 * c),
    ("影音廣告", 0, 0),
]
target = 2.5 + 0.1 * c

# 定義廣告成效函式
def ad_report(impressions, clicks, target=3.0):
    if impressions == 0:
        return (None, False)

    ctr = clicks / impressions * 100
    passed = ctr >= target
    return (ctr, passed)


# 印出廣告成效報表
print("學號：", student_id)
print(f"CTR門檻：{target:.2f}%")

passed_count = 0

for name, impressions, clicks in ads:
    ctr, passed = ad_report(
        impressions,
        clicks,
        target=target
    )

    if ctr is None:
        ctr_text = "無曝光資料"
    else:
        ctr_text = f"{ctr:.2f}%"

    print(
        f"{name}：曝光={impressions}，點擊={clicks}，"
        f"CTR={ctr_text}，達標={passed}"
    )

    if passed:
        passed_count += 1

print("達標廣告數：", passed_count)

# 額外測試：預設門檻與零點擊
print("預設門檻測試：", ad_report(1000, 30))
print("零點擊測試：", ad_report(1000, 0))
