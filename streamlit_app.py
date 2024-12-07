import streamlit as st
import random
import pygame
from io import BytesIO

# 初期化
pygame.mixer.init()

# リンパマッサージ場所とその説明、マッサージ方法
lymphatic_points = {
    "首（首筋、鎖骨周辺）": {
        "description": "首と鎖骨周辺にはリンパ節が集中しており、ここをマッサージすることで顔や首周りのむくみを改善できます。",
        "massage_method": "首を軽く引き寄せるようにして、指の腹を使って円を描くように優しくマッサージします。鎖骨の上部も軽く押しながらマッサージしましょう。",
    },
    "脇の下（腋窩リンパ節）": {
        "description": "脇の下は上半身のリンパが集まる重要な場所です。ここをマッサージすると、肩こりや腕の疲れにも効果的です。",
        "massage_method": "脇の下に指を入れ、親指と人差し指でリンパの流れを促進するように優しく押して動かします。力を入れすぎないように注意しましょう。",
    },
    "膝裏（膝窩リンパ節）": {
        "description": "膝裏には下半身のリンパが集まる場所があり、特にむくみやすい部分です。膝裏をマッサージすることで足のむくみを解消できます。",
        "massage_method": "膝を軽く曲げた状態で、膝裏に両手を当てて円を描くように優しくマッサージします。足の指先まで流れるように意識して行いましょう。",
    },
    "足首（足首リンパ節）": {
        "description": "足首は足全体のリンパの流れに大きく影響します。足首周辺をマッサージすることで、足のむくみを軽減することができます。",
        "massage_method": "足首の周りを指の腹で優しく円を描くようにマッサージします。足の指先から膝に向かってリンパの流れを意識して行います。",
    },
    "顔（顔面リンパ節）": {
        "description": "顔には多くのリンパ節があり、特に顔のむくみや小顔効果を期待する場合に重要な場所です。",
        "massage_method": "顔全体を軽く引き上げるようにして、指の腹で額から顎にかけて優しく流します。耳の後ろまで流れるように意識して行いましょう。",
    }
}

# 人体と精神に関する豆知識
human_facts = [
    "人体には約10万キロメートルの血管があり、これを繋げると地球を2周半できます。",
    "精神的な健康と身体の健康は密接に関わっており、リラックスした状態が免疫力を高めます。",
]

# 人体に関する簡単な問題
body_question = {
    "問題": "人体における最大の臓器はどれでしょう？",
    "選択肢": ["心臓", "皮膚", "肝臓", "脳"],
    "正解": "皮膚"
}

# アプリのタイトルと説明
st.title("今日の夜、リンパマッサージをするべき場所")
st.write("リラックスした夜を過ごすために、リンパマッサージをしましょう！")
st.write("下記の3つのリンパマッサージ場所をランダムに提案します。")

# ボタンを押してランダムに3つの場所を提案
if st.button("リンパマッサージ場所を提案"):
    selected_points = random.sample(list(lymphatic_points.keys()), 3)

    for i, point in enumerate(selected_points, 1):
        st.write(f"### {i}. {point}")
        st.write(f"**説明**: {lymphatic_points[point]['description']}")
        st.write(f"**マッサージ方法**: {lymphatic_points[point]['massage_method']}")
        st.write("")  # 空行を挿入

    # 応援メッセージ
    st.write("素晴らしい！リンパマッサージでリラックスして、心と体をケアしましょう！")

    # 豆知識
    st.write("#### 今日の豆知識:")
    st.write(random.choice(human_facts))

    # 音楽再生
    st.write("リラックスした雰囲気でリンパマッサージを楽しんでください。下の音楽を聴いてリラックスしましょう。")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

    # 簡単な問題
    st.write(f"#### 問題: {body_question['問題']}")
    st.write("選択肢:")
    for choice in body_question['選択肢']:
        st.write(f"- {choice}")

    # 正解を表示するボタン
    if st.button("答えを表示"):
        st.write(f"正解は: {body_question['正解']}です！")

