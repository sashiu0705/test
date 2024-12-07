import streamlit as st
import random

# 食材と料理リスト
ingredients = {
    "野菜": ["キャベツ", "ほうれん草", "にんじん", "大根", "玉ねぎ", "トマト", "ブロッコリー"],
    "肉": ["鶏肉", "豚肉", "牛肉", "ひき肉"],
    "魚": ["サバ", "サーモン", "アジ", "イワシ"],
    "豆腐・卵": ["豆腐", "卵", "納豆"],
    "炭水化物": ["ご飯", "うどん", "パスタ", "そば", "パン"]
}

# 料理の提案リスト（仮）
dishes = {
    "野菜": ["野菜炒め", "サラダ", "煮物", "グラタン"],
    "肉": ["唐揚げ", "肉じゃが", "焼肉", "チキンカツ"],
    "魚": ["焼き魚", "煮魚", "刺身", "魚のフライ"],
    "豆腐・卵": ["豆腐の味噌汁", "卵焼き", "オムレツ", "親子丼"],
    "炭水化物": ["ご飯", "うどん", "スパゲティ", "チャーハン"]
}

# StreamlitのUI部分
st.title("今日の晩御飯献立")
st.write("食材を選んで、今日の晩御飯の献立を決めましょう！")

# 食材選択
selected_ingredients = {}
for category, items in ingredients.items():
    selected_ingredients[category] = st.multiselect(f"{category}を選んでください", items)

# メニューの決定
if st.button("献立を決める"):
    selected_dishes = []
    for category, selected_items in selected_ingredients.items():
        if selected_items:
            selected_dishes.append(random.choice(dishes[category]))

    if selected_dishes:
        st.write("今日の晩御飯の献立は:")
        for dish in selected_dishes:
            st.write(f"- {dish}")
    else:
        st.write("食材を選んでください！")
