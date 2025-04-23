#import streamlit as st

# Main page content
#st.markdown("# Main page 🎈")
#st.sidebar.markdown("# Main page 🎃")
import streamlit as st

st.set_page_config(
    page_title="🌍 SDGs 프로젝트 대시보드",
    page_icon="📊",
    layout="wide",
)

st.title("🌍 SDGs 분석 대시보드 by 석리송🎵")

st.markdown(
    """
안녕하세요! 🎉  
이 대시보드는 **지속가능개발목표(SDGs)** 관점에서 국가별 주요 지표(1인당 GDP · 기대수명 · 인구 수 등)를 Streamlit + Plotly로 **직접 탐구**할 수 있도록 구성되었습니다.  

왼쪽 사이드바에서 관심 있는 주제를 클릭해 보세요! 

- 🏥 **전세계 기대수명 변화**  
  “전세계 기대수명은 어떻게 변화했을까?”  

- 💸 **저소득국 비율 변화**  
  “극빈곤 국가 비율은 어떤 추세일까?”  

- 🚀 **GDP 성장률 Top10**  
  “어떤 국가들이 가장 빠르게 경제성장했을까?”  

- 🔍 **소득격차 분포**  
  “소득격차는 어떻게 줄어들고 있을까?”  

- 🔗 **기대수명 · GDP 상관관계**  
  “경제 성장과 건강 수준은 어떤 관계일까?”  

- 👥 **인구증가 Top10**  
  “어디에서 인구가 가장 많이 늘어났을까?”  

- 📈 **소득그룹별 GDP 추세**  
  “저·중·고소득 그룹의 성장 양상은 어떻게 다를까?”  

- 🌐 **권역별 저소득국 수**  
  “아시아·아프리카·미주·유럽, 어느 곳의 빈곤국이 줄어들었을까?”  

- 🔮 **2100 비교 분석**  
  “다가올 미래, 국가별 2100년의 지표들은 어떻게 전개될까?”  

---

✨ **지금 바로** 왼쪽 메뉴를 눌러 호버, 슬라이더, 멀티셀렉트 등 다양한 인터랙티브 컨트롤을 활용하며 직접 데이터 속으로 뛰어들어 보세요!  
"""
)

st.sidebar.markdown("# 🏥 **전세계 기대수명 변화** ")
st.sidebar.markdown("# 💸 **저소득국 비율 변화** ")
st.sidebar.markdown("# 🚀 **GDP 성장률 Top10** ")
st.sidebar.markdown("# 🔍 **소득격차 분포**  ")
st.sidebar.markdown("# 🔗 **기대수명 · GDP 상관관계** ")
st.sidebar.markdown("# 👥 **인구증가 Top10**   ")
st.sidebar.markdown("# 📈 **소득그룹별 GDP 추세** ")
st.sidebar.markdown("# 🌐 **권역별 저소득국 수** ")
st.sidebar.markdown("# 🔮 **2100 비교 분석** ")
