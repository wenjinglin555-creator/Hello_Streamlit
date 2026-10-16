import streamlit as st

# ==========================================
# 1. 基本資料設定（可以改成你自己的資料）
# ==========================================
my_name = "林汶靚"                # 你自己的姓名
my_class = "高一 11 班"            # 你自己的班級
my_id = "511120"               # 你自己的學號
my_group = "高一自主學習組"               # 組別 (自然組改為"高一自主學習組")
my_skills = ["Python", "VS Code", "GitHub", "Streamlit Cloud"]  # 修正 ??


# ==========================================
# 2. 側邊欄：個人名片
# ==========================================
st.set_page_config(page_title=f"{my_name} 的個人網頁", page_icon="💻")

with st.sidebar:
    st.header("👤 學生個人資訊")
    # 顯示個人頭像（預設為網路小圖示）
    st.image("https://cdn-icons-png.flaticon.com/512/3242/3242257.png", width=100)

    # 顯示基本資料
    st.write(f"**姓名：** {my_name}")
    st.write(f"**班級：** {my_class}")
    st.write(f"**學號：** {my_id}")
    st.write(f"**組別：** {my_group}")

    st.divider()
    st.subheader("🛠 我學會的工具")
    for skill in my_skills:
        st.write(f"- {skill}")

# ==========================================
# 3. 主畫面：打招呼與 if / else 判斷練習
# ==========================================
st.title("✨ 我的第一個 Python 互動網頁")
st.write(f"你好！我是 **{my_name}**，這是我用 Python 製作的小作品。")
st.divider()

# 讓使用者在網頁上輸入文字（提示文字同步加入「委員」範例）
visitor = st.text_input("請輸入你的名字或稱呼：", placeholder="例如：王小華、李老師、林委員、陳曉明同學")

# ------------------------------------------
# 核心觀念：if - elif - else 條件判斷
# ------------------------------------------
# 第一層判斷：先檢查「有沒有輸入內容」？ 如果沒有輸入內容 如果有輸入內容 
if visitor == "":
    st.info("👆 請在上方格子輸入名字，按下 Enter 看看會發生什麼事！")

else:
    # 第二層判斷：根據輸入的關鍵字，做出不同的回應
    if "老師" in visitor or "委員" in visitor:
        st.balloons()  # 放氣球慶祝動畫
        st.success(f"🎉 歡迎 {visitor} 蒞臨指導！感謝您的鼓勵！")
        st.write("觸發條件：名字裡有「老師」或「委員」")

    elif "同學" in visitor:
        st.snow()  # 畫面下雪特效
        st.info(f"### 嗨！{visitor}，今天上課加油！❄️")
        st.write("觸發條件：名字裡有「同學」")

    else:
        st.write(f"### 哈囉，{visitor}！很高興認識你！😊")
        st.write("觸發條件：以上條件都不符合時，走這條路（預設回應）")

st.divider()
st.caption(f"© 2026 {my_name} | 高一自主學習成果")


