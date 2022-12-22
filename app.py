import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.express as px
import altair as alt  
from sklearn.preprocessing import LabelEncoder

from pyparsing import empty
from tkinter.tix import COLUMN

# 이 코드는 ec2에 한글 폰트가 설치되어 있어야 하고,
# 파이썬에서 한글 사용가능토록 먼저 셋팅해야 한다.
# https://luvris2.tistory.com/119#1.4.%20matplotlib%EC%97%90%20%ED%95%9C%EA%B8%80%20%ED%8F%B0%ED%8A%B8%20%ED%99%95%EC%9D%B8

import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    rc('font', family='NanumGothic')

# 레이아웃 설정
st.set_page_config(layout="wide")
empty1,con1,empty2 = st.columns([0.2,0.5,0.2])
empyt1,con2,con3,empty2 = st.columns([0.3,0.2,0.5,0.3])
empyt1,con4,empty2 = st.columns([0.3,0.7,0.3])
empyt1,con4_1,empty2 = st.columns([0.3,0.7,0.3])
empyt1,con5,con6,empty2 = st.columns([0.3,0.35,0.35,0.3])
empyt1,con6_1,empty2 = st.columns([0.3,0.7,0.3])
empyt1,con7,con8,empty2 = st.columns([0.3,0.35,0.35,0.3])


def main() :
    
    df = pd.read_csv('data/League of Legends Champion Stats 12.1.csv', sep =';')
    df.dropna(inplace=True)

    # 차트를 위한 레이블링
    df1= df.copy()
    df1['Win %']=df1['Win %'].str.replace('%', '').astype(float) 
    df1['Role %']=df1['Role %'].str.replace('%', '').astype(float) 
    df1['Pick %']=df1['Pick %'].str.replace('%', '').astype(float) 
    df1['Ban %']=df1['Ban %'].str.replace('%', '').astype(float) 
    with empty1 :
        
        empty()# 좌 여백부분1
        
    with con1 :
        st.image('https://cloudfront-us-east-1.images.arcpublishing.com/infobae/YABJ7CAXOZDVHAXSDRSQQ7NJR4.jpg')
        st.header('League of Legends Champion Stats 12.1')
        # st.area_chart(df['Win %'].head(3))
        

    with con2 :
        
        choice = st.radio('해당티어만 보기', ['전체', 'God','S', 'A', 'B', 'C', 'D'])
        character = st.text_input('캐릭터 풀네임을 검색해보세요', 'Search')
        # 해당 영웅의 이미지 예정
    
    with con3 :

        if choice == '전체' :
            st.dataframe(df)
        elif choice == 'God' :
            st.dataframe(df[df['Tier'] == 'God'])
        elif choice == 'S' :
            st.dataframe(df[df['Tier'] == 'S'])
        elif choice == 'A' :
            st.dataframe(df[df['Tier'] == 'A'])
        elif choice == 'B' :
            st.dataframe(df[df['Tier'] == 'B'])
        elif choice == 'C' :
            st.dataframe(df[df['Tier'] == 'C'])
        elif choice == 'D' :
            st.dataframe(df[df['Tier'] == 'D'])
        if character != 'Search' and character != '':
            st.warning('검색결과는 여기에 표시됩니다')
            st.dataframe(df[df['Name'] == character.capitalize()])
        
    with con4:
        if character != 'Search' and character != '':
            hero_selceted = st.selectbox('다른 영웅을 선택하고 싶다면 검색을 비우세요.', df[df['Name'] == character.capitalize()])
            st.image(f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{hero_selceted}_0.jpg')
        else:
            hero_selceted = st.selectbox('영웅을 골라보세요', df['Name'].unique())
            st.image(f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{hero_selceted}_0.jpg')
        
       
    with con4_1:
        st.subheader(f'{hero_selceted}의 전투력을 확인합니다.')
        hero_df = df1.loc[ df1['Name'] == hero_selceted]
        

        # 평균과 비교해서 높은지 낮은지 표시
     

       


    with con5 :
    
        # 선택한 영웅의 데이터를 pie chart로 표현
        pass
       

        
        # fig = px.line(df, x='Name', y='Win %', title='Win %')
        # fig.add_scatter(x=df['Name'], y=df[df['Name'] == hero_selceted]['Win %'], mode='lines', name=hero_selceted)
        # st.plotly_chart(fig)


        
    with con6 :
        # 여러가지 차트를 선택할 수 있는 버튼을 만들어서 선택하면 해당 차트가 나오도록
        pass
        # st.button('Pick %')
        # st.button('Ban %')
        # st.button('KDA')
        # pie chart, bar chart
        
    

    

    with con6_1 :
        st.subheader('어떤 클래스가 트렌디한지 확인합니다.')


    with con7 :
        
        st.markdown('''
        -----------
        ''')
        st.text('클래스별 트렌드')
        st.bar_chart(df1.groupby('Class')['Trend'].mean())
		
        st.markdown('''
        -----------
        ''')


       
    with con8 :
        st.markdown('''
        -----------
        ''')
        st.text('클래스별 스코어')
        st.bar_chart(df1.groupby('Class')['Score'].mean())

        st.markdown('''
        -----------
        ''')
    with empty2 :
       pass





if __name__ == '__main__' :
    main()
