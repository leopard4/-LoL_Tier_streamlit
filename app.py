import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import io
import requests
from pyparsing import empty
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# 이 코드는 ec2에 한글 폰트가 설치되어 있어야 하고,
# 파이썬에서 한글 사용가능토록 먼저 셋팅해야 한다.
# https://luvris2.tistory.com/119#1.4.%20matplotlib%EC%97%90%20%ED%95%9C%EA%B8%80%20%ED%8F%B0%ED%8A%B8%20%ED%99%95%EC%9D%B8

# 리눅스에서 한글처리를 위한 코드
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
empyt1,con5, empty2 = st.columns([0.3,0.7,0.3])
empyt1,con6_1,empty2 = st.columns([0.3,0.7,0.3])
empyt1,con7,con8,empty2 = st.columns([0.3,0.35,0.35,0.3])
empyt1,con8_1,empty2 = st.columns([0.3,0.7,0.3])



def main() :
    
    # 데이터를 가져와서 null 처리
    df = pd.read_csv('data/League of Legends Champion Stats 12.1.csv', sep =';')
    df.dropna(inplace=True)
    # 사이드 이미지를 가져오기 위한 코드
    df['Name'] = df['Name'].str.replace(' ', '')
    df['Name'] = df['Name'].str.replace('\'', '')
    df['Name'] = df['Name'].str.replace('.', '')
    for i in df['Name'].unique():
        st.sidebar.image(f'https://opgg-static.akamaized.net/meta/images/lol/champion/{i}.png?image=c_crop,h_103,w_103,x_9,y_9/q_auto,f_webp,w_160&v=1671624147144')
        st.sidebar.text(i)
    

    # 차트를 그리기위한 숫자로 만드는 코드
    df1= df.copy()
    df1['Win %']=df1['Win %'].str.replace('%', '').astype(float) 
    df1['Role %']=df1['Role %'].str.replace('%', '').astype(float) 
    df1['Pick %']=df1['Pick %'].str.replace('%', '').astype(float) 
    df1['Ban %']=df1['Ban %'].str.replace('%', '').astype(float) 
    
    with empty1 :
        
        empty()# 좌 여백부분1
        
    with con1 :
        
        # 타이틀 이미지와 제목
        url = 'https://cloudfront-us-east-1.images.arcpublishing.com/infobae/YABJ7CAXOZDVHAXSDRSQQ7NJR4.jpg'
        response = requests.get(url)
        image_data = response.content
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((1200, 300),resample=Image.BICUBIC)
        st.image(image)
        st.header('League of Legends Champion Stats 12.1')
       
    with con2 :
        
        # 티어 고르는 라디오 버튼 / 검색창
        choice = st.radio('해당티어만 보기', ['전체', 'God','S', 'A', 'B', 'C', 'D'])
        character = st.text_input('캐릭터 풀네임을 검색해보세요', 'Search')
        st.write("이름이 기억이 나지않는다면 좌측 슬라이드바를 확인하세요")
       
    with con3 :
        
        # 고른 티어를 데이터 프레임으로 보여줌
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

        # 검색한 캐릭터의 이미지를 가져와서 보여줌
        if character != 'Search' and character != '':
            hero_selceted = st.selectbox('다른 영웅을 선택하고 싶다면, 최근 검색을 비워야만 합니다.', df[df['Name'] == character.capitalize()])
            url = f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{hero_selceted}_0.jpg'
            response = requests.get(url)
            
            # html 헤더가 이미지가 맞는지 확인
            if response.headers['Content-Type'].startswith('image'):
                image_data = response.content
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((1400, 300),resample=Image.BICUBIC)
                st.image(image)
            
        else:
            
            hero_selceted = st.selectbox('영웅을 골라보세요', df['Name'].unique())
            url = f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{hero_selceted}_0.jpg'
            response = requests.get(url)

            if response.headers['Content-Type'].startswith('image'):
                image_data = response.content
                image = Image.open(io.BytesIO(image_data))
                image = image.resize((1400, 300),resample=Image.BICUBIC)
                st.image(image)
                
           
        
       
    with con4_1:
        
        # 선택한 데이터에 동일한 영웅이 존재할수있으므로
        # 그중 첫번째 행만 가져옴
        hero = df1.loc[ df1['Name'] == hero_selceted]
        Role_group = df1.groupby('Role')[['Win %','Score','Trend','KDA']].agg(np.mean).reset_index()
        hero_val = hero['Role'].values[0]
        if len(hero) > 1 :
            hero = pd.DataFrame(hero.iloc[0]).T
        choose_role = Role_group.loc[Role_group['Role'].values == hero_val , ]
        choose_role.set_index(choose_role['Role'].values+'_mean',inplace=True)
        hero.set_index('Name',inplace=True)
        hero.drop(['Class','Role','Tier','Role %','Pick %','Ban %'], axis=1 ,inplace=True)
        choose_role.drop('Role',axis=1,inplace=True)
        last_df = pd.concat([hero, choose_role], axis=0)
        last_df.reset_index(inplace=True)

    with con5 :
        
        # 선택한 영웅의 데이터를 서브플롯으로 보여줌
        fig = make_subplots(rows=2, cols=2,subplot_titles=last_df.columns[1:])
        fig.add_trace(
            go.Scatter(x=last_df['index'], y=last_df['Score'],name="Score",
                
                mode="markers+text",
                text=last_df['index'].values,
                textposition="bottom center"
                    
                    ),
            row=1, col=1
        )

        fig.add_trace(
            go.Scatter(x=last_df['index'], y=last_df['Trend'],name='Trend',
                    mode="markers+text",
                text=last_df['index'].values,
                textposition="bottom center"
                    ),
            row=1, col=2
        )

        fig.add_trace(
            go.Scatter(x=last_df['index'], y=last_df['Win %'],name='Win %',
                    mode="markers+text",
                text=last_df['index'].values,
                textposition="bottom center"),
            row=2, col=1
        )
        fig.add_trace(
            go.Scatter(x=last_df['index'], y=last_df['KDA'],name='KDA',
                    mode="markers+text",
                text=last_df['index'].values,
                textposition="bottom center"),
            row=2, col=2
        )

        fig.update_layout(height=600, width=800,legend_title="Legend", title_text="선택한 영웅과 같은 포지션의 평균 스탯을 비교합니다")

        fig.update_xaxes(title_text="영웅점수", range=[-1,2],row=1, col=1)
        fig.update_xaxes(title_text="트렌드점수", range=[-1,2], row=1, col=2)
        fig.update_xaxes(title_text="승률", range=[-1,2], showgrid=False, row=2, col=1)
        fig.update_xaxes(title_text="킬뎃", range=[-1,2],row=2, col=2) # 파라미터 type="log"

        fig.update_yaxes(title_text="", row=1, col=1)
        fig.update_yaxes(title_text="", range=[-15, 15], row=1, col=2)
        fig.update_yaxes(title_text="", showgrid=False, row=2, col=1)
        fig.update_yaxes(title_text="", row=2, col=2)
        
        st.plotly_chart(fig)


    with con6_1 :

        # 좋은 클래스와 좋은 라인을 확인합니다.
        st.markdown('''
        -----------
        ''')
        fig = make_subplots(rows=1, cols=2)

        fig.add_trace(go.Bar(x=df['Class'].unique(), y=df.groupby('Class')['Score'].mean().sort_values(ascending=False),
                            ),
                    1, 1)

        fig.add_trace(go.Bar(x=df['Role'].unique(), y=df.groupby('Role')['Score'].mean(),
                            ),
                    1, 2)

        fig.update_layout(coloraxis=dict(colorscale='Bluered_r'), showlegend=False,title_text="좋은 클래스와 좋은 라인을 확인합니다.")
        fig.update_xaxes(title_text="클래스별 평균 Score",row=1, col=1)
        fig.update_xaxes(title_text="라인별 평균 Score",row=1, col=2)

        st.plotly_chart(fig)

        st.markdown('''
        -----------
        ''')

    with con7 :
        pass

    with con8 :
        pass
        
    with con8_1 :

        # 선택한 영웅과 비슷한 추천영웅 데이터 프레임으로 표시
        st.subheader('선택한 영웅과 같은 포지션의 좋은 영웅을 추천합니다.')
        suggestion = df1.loc[ df1['Role'] == hero_val, ]
        st.dataframe(suggestion.sort_values('Score',ascending=False).head(5))

        # 버튼을 누르면 상관관계를 표시함
        if st.button('더 알고싶다면 누르세요') :     
            st.write('1에 가까울수록 비례관계 -1에 가까울수록 반비례 관계를 하나의 표로 표현한 것입니다.')           
            fig = plt.figure()
            sns.heatmap(df1.corr(), annot=True, cmap='coolwarm', center=0, fmt='.1f', linewidths=1, linecolor='white')
            plt.title('상관관계')
            st.pyplot(fig)
            st.write('분석결과 Score와 pick % 은 아주 강한 비례관계에 있음을 알 수 있고')
            st.write('Score와 ban % 은 비례관계임을 알수있습니다.')
            st.write('결론적으로 Score가 높을수록 게임에 영향이 큰 캐릭터라고 유추할수있습니다.')

    with empty2 :
       pass


if __name__ == '__main__' :
    main()
