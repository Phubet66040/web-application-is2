#ติดตั้งก่อนในเทอมินอล  pip install pandas streamlit


import streamlit as st #นำเข้าตัวทำเว็ป
import pandas as pd #นำเข้าตัววิเคราะห์ข้อมูล


st.title("📊 รายได้ครัวเรือนในไทย")

# 🔹 โหลดข้อมูลที่บันทึกจาก NeuronTest.py
try:
    df = pd.read_pickle("processed_data.pkl")  # โหลดจาก Pickle (เร็ว)
except:
    df = pd.read_csv("processed_data.csv", encoding="utf-8-sig")  # โหลดจาก CSV

# 🔹 แสดงข้อมูล
st.write("📌 ข้อมูลที่โหลดมาจาก NeuronTest.py:")
st.dataframe(df.head())

# 🔹 เลือกช่วงรายได้
income_range = st.selectbox("เลือกช่วงรายได้ที่ต้องการดู", 
                            [100000, 500000, 1000000, 5000000, 10000000])

# 🔹 กรองข้อมูล
filtered_df = df[df["MONTHLY_INCOME"] >= income_range]

st.write(f"📌 คนที่มีรายได้มากกว่า {income_range} บาท/เดือน")
st.dataframe(filtered_df)
