

import streamlit as st
import  pandas as pd
import numpy as np
from datetime import datetime as dt
import datetime


st.title("이것이 타이틀이다.")
st.header("이것이 헤더이다.")
st.subheader("이것이 서브헤더이다.")
st.text("스마일:😒")

st.caption("이것이 캡션이다.")
st.markdown("*이것이* **마크다운** 이다., **굵게**, __굵게__, *기울임*, _기울임_")
st.markdown("안녕하세요 **Streamlit** 입니다 😄")

sample_code = '''
def hello():
    print("Hello, Streamlit!")
hello()
'''
st.code(sample_code, language='python')

#마크다운으로 코드 작성하기
st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼드체를 설정할 수 있다.")

#마크다운 문법 지원
st.markdown("텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼드체를 설정할 수 있다.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$]와 같은 수식도 지원한다.")

st.latex(r'\sqrt{x^2+y^2}=1')

#dataframe 생성
dataframe=pd.DataFrame({
    "first colunm": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
})

#dataframe 

st.dataframe(dataframe) #(수정가능 오름차순 내림차순가능. 유동적일때)

#테이블 출력
st.table(dataframe)#(고정일때)

#메트릭
st.metric(label="온도", value="25°C", delta="+3°C")
st.metric(label="삼성전자", value="140,000원", delta="3800원")

#컬럼으로 영역 나누어 표기
col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1471", delta="30원")
col2.metric(label="유로", value="1571", delta="20원")
col3.metric(label="일본엔", value="1071", delta="70원")

#버튼클릭

button=st.button("버튼을 눌러주세요")
if button:
    st.write(":blue[버튼]이 눌렸습니다.👍")

agree = st.checkbox("체크박스를 눌러주세요")
if agree:
    st.write("체크박스가 선택되었습니다.✅")

    #라디오 버튼
mbti = st.radio("당신의 MBTI는 무엇인가요?", ('ENFP', 'INFP', 'INTJ', 'ISTJ'), index=1) 
st.write("당신의 MBTI는 :green[", mbti, "]입니다.")     

if mbti == 'ENFP':
    st.write("당신은 모험을 즐기는 사람입니다.🏕️")
elif mbti == 'INFP':
    st.write("당신은 이상주의자입니다.🌈")
elif mbti == 'INTJ':
    st.write("당신은 전략가입니다.♟️")
else:
    st.write("당신은 현실주의자입니다.🏢" )


#셀렉트박스
favorite_color = st.selectbox(
    '당신이 좋아하는 색깔은 무엇인가요?',
    ('빨강', '파랑', '초록', '노랑')
)

st.write('당신이 좋아하는 색깔은  :red[{favorite_color}] 입니다.')



if favorite_color == '빨강':
    st.write("당신은 열정적인 사람입니다.❤️")   


#슬라이더
age = st.slider('당신의 나이는 몇 살인가요?', 0, 120, 25)
st.write(f'당신의 나이는 :blue[{age}]살 입니다.')

value = st.slider(
    "범위의 값을 다음과 같은 범위로 설정하세요",
    0.0, 100.0, (25.0, 75.0)
)

st.write(f"선택한 범위는 :green[{value}] 입니다.")




#날짜 선택
start_time=st.slider(
    "언제 약속을 잡는 것이 좋을까요?",
    min_value=dt(2026, 1, 1, 0, 0),
    max_value=dt(2026, 12, 31, 0, 0),
    value=dt(2026, 1, 15, 12, 0),
    step=datetime.timedelta(days=1),
    format="YYYY-MM-DD HH:mm"
)
st.write(f"약속 날짜는 :green[{start_time}]입니다.")

#텍스트 입력
title=st.text_input(
    label="가고 싶은 여행지가 있나요?",
    placeholder="예: 제주도, 부산, 뉴욕"
)
st.write(f"당신이 가고 싶은 여행지는 :green[{title}]입니다.")

#숫자 입력
number=st.number_input(
    label="당신이 좋아하는 숫자는 무엇인가요?",
    min_value=0,
    max_value=100,
    value=50,
    step=1

)
st.write(f"당신이 좋아하는 숫자는 :green[{number}]입니다.")

#파일다운로드 버튼
st.download_button(
    label="CSV 다운로드",
    data=dataframe.to_csv(index=False).encode('utf-8'),
    file_name="sample.txt",
    mime="text/csv"
)