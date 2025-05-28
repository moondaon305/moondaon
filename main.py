import streamlit as st
st.title('나의 첫 Streamlit 앱')
st.write('안녕하세요!')

import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="데이터 시각화", layout="wide")

st.title("Google Drive CSV 데이터 시각화")

# 데이터 로드
@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
    df = pd.read_csv(url)
    return df

df = load_data()

st.subheader("원본 데이터")
st.dataframe(df)

# 컬럼 선택
numerical_cols = df.select_dtypes(include='number').columns.tolist()
categorical_cols = df.select_dtypes(include='object').columns.tolist()

x_axis = st.selectbox("X축 변수 선택", numerical_cols)
y_axis = st.selectbox("Y축 변수 선택", numerical_cols, index=1 if len(numerical_cols) > 1 else 0)
color_col = st.selectbox("색상 그룹화 기준 (선택)", ["없음"] + categorical_cols)

# 그래프 생성
st.subheader("Plotly 시각화")
if color_col == "없음":
    fig = px.scatter(df, x=x_axis, y=y_axis)
else:
    fig = px.scatter(df, x=x_axis, y=y_axis, color=df[color_col])

st.plotly_chart(fig, use_container_width=True)
