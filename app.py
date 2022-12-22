import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.express as px
from sklearn.preprocessing import LabelEncoder
from PIL import Image
import io
import requests

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
empyt1,con8_1,empty2 = st.columns([0.3,0.7,0.3])

# 이미지 크기조정을 위한 함수

def main() :
    
    df = pd.read_csv('data/League of Legends Champion Stats 12.1.csv', sep =';')
    df.dropna(inplace=True)
    # 이름 가공
    df['Name'] = df['Name'].str.replace(' ', '')
    df['Name'] = df['Name'].str.replace('\'', '')
    df['Name'] = df['Name'].str.replace('.', '')
    for i in df['Name'].unique():
        st.sidebar.image(f'https://opgg-static.akamaized.net/meta/images/lol/champion/{i}.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto,f_webp,w_160&v=1671624147144')
        st.sidebar.text(i)
    

    # 차트를 위한 레이블링
    df1= df.copy()
    df1['Win %']=df1['Win %'].str.replace('%', '').astype(float) 
    df1['Role %']=df1['Role %'].str.replace('%', '').astype(float) 
    df1['Pick %']=df1['Pick %'].str.replace('%', '').astype(float) 
    df1['Ban %']=df1['Ban %'].str.replace('%', '').astype(float) 
    with empty1 :
        
        empty()# 좌 여백부분1
        
    with con1 :
        url = 'https://cloudfront-us-east-1.images.arcpublishing.com/infobae/YABJ7CAXOZDVHAXSDRSQQ7NJR4.jpg'
        response = requests.get(url)
        image_data = response.content
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((1200, 300),resample=Image.BICUBIC)
        st.image(image)
        st.header('League of Legends Champion Stats 12.1')
        # st.area_chart(df['Win %'].head(3))
        # 'https://cloudfront-us-east-1.images.arcpublishing.com/infobae/YABJ7CAXOZDVHAXSDRSQQ7NJR4.jpg'
    with con2 :
        
        choice = st.radio('해당티어만 보기', ['전체', 'God','S', 'A', 'B', 'C', 'D'])
        character = st.text_input('캐릭터 풀네임을 검색해보세요', 'Search')
        st.write("이름이 기억이 나지않는다면 좌측 슬라이드바를 확인하세요")
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
            hero_selceted = st.selectbox('다른 영웅을 선택하고 싶다면, 최근 검색을 비워야만 합니다.', df[df['Name'] == character.capitalize()])
            url = f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{hero_selceted}_0.jpg'
            response = requests.get(url)
            image_data = response.content
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((1200, 300),resample=Image.BICUBIC)
            st.image(image)
            
        else:
            hero_selceted = st.selectbox('영웅을 골라보세요', df['Name'].unique())
            url = f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{hero_selceted}_0.jpg'
            response = requests.get(url)
            image_data = response.content
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((1200, 300),resample=Image.BICUBIC)
            st.image(image)
           
        
       
    with con4_1:
        st.subheader(f'{hero_selceted}의 전투력을 확인합니다.')
        hero_df = df1.loc[ df1['Name'] == hero_selceted]
        

        # 평균과 비교해서 높은지 낮은지 표시
     

       


    with con5 :
    
        # 선택한 영웅의 데이터를 pie chart로 표

        pass
        # fig = plt.figure()
        # plt.scatter(x=df['Name'], y=df[df['Name'] == hero_selceted]['Win %'], mode='lines', name=hero_selceted)
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
        st.dataframe(df1.groupby('Class')['Trend'].mean().sort_values(ascending=False))  


        st.markdown('''
        -----------
        ''')


       
    with con8 :
        st.markdown('''
        -----------
        ''')
        st.text('클래스별 스코어')
        st.bar_chart(df1.groupby('Class')['Score'].mean())
        st.dataframe(df1.groupby('Class')['Score'].mean().sort_values(ascending=False))  

        st.markdown('''
        -----------
        ''')
    with con8_1 :
        if st.button('<<<<<<<상관관계 분석 버튼>>>>>>>>>>') :                
            fig = plt.figure()
            sns.heatmap(df1.corr(), annot=True, cmap='coolwarm', center=0, fmt='.1f', linewidths=1, linecolor='white')
            plt.title('상관관계')
            st.pyplot(fig)
            st.write('분석결과 Score와 pick % 은 아주 강한 상관관계에 있음을 알 수 있습니다.')
        

    


    with empty2 :
       pass





if __name__ == '__main__' :
    main()
