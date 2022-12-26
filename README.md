<h1 align="center">LoL_Tier_streamlit </h1>
<h3 align="center">좋은영웅을 판단하여 사용자에게 추천하는 웹 대시보드</h3>
<img src= "https://user-images.githubusercontent.com/95200973/209294754-6157fe5b-1a8e-4898-9db9-4bf5ab5d0148.png" width="1000">  


<h4 align="left">사용한 언어 & 툴:</h4>
<p align="left">  
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/>
<img src="https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=Streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=Jupyter&logoColor=white"/>
<img src="https://img.shields.io/badge/Plotly-3F4F75?style=flat-square&logo=Plotly&logoColor=white"/>

</p>

## - :closed_book: 진행 과정

### 1. 데이터셋 탐색 및 선택 과정    
데이터분석에서는 유명하다고 알려진 kaggle에서  
유용한 데이터를 필터로 검색하였고  
게이머에겐 유용하기도 하고   
만들기도 재미있어 보이는 롤 통계 데이터를 선택하였습니다.  

### 2. 웹 대시보드 기획  
여기선 어떤걸 사용자가 원할지 먼저 생각해보고   
생각한 내용중 가장 적합하다고 생각되는 기능들을 메모해놓고   
배치는 어떻게 해야할지 어떻게해야 친절한 설명이 될지에대해   
고민을하고 그려가며 기획을 하였습니다.   

### 3. 데이터 분석  
데이터셋의 글쓴이가 데이터로 하고자 했던 의도를 파악하고  
관련 분석글을 보면서 분석하고자하는 방향을 잡았고,  
머신러닝 관련 지식도 공부중이였기 때문에   
분류(Classification)의 방법중 하나인   
가우시안NB를 이용하여 학습시킨 인공지능으로   
활용해 볼려고 하였지만, 중요한 데이터들은 이미 분류가 되어있었기에  
큰 의미는 없다고 생각되어  
방향을 바꿔 해당영웅과 비슷한 영웅을 추천하는 방향으로 최종 결정했습니다.  

### 4. 사용자 인터랙티브한 동적 차트를 구현하기위한 노력  
기존에 학습하였던 matplolib과 seabon 차트는   
streamlit 웹 대시보드를 동적으로 구현하는대에 어려움을 느꼈기 때문에   
더 좋은 방법을 검색한 끝에   
plotly라는 대쉬보드에 특화된 라이브러리를 알게되었고    
해당 레퍼런스를 참조하며 서브플롯을 구현했습니다.     

### 5. 테스트 및 배포   
로컬에서 예상치 못한 버그나 오류는 없는지 수차례 확인하였고   
웹 대시보드의 용도로써는 충분하다고 판단되어  
git에 push 하였으며  
AWS에서 미리 만들어 두었던 EC2서버에 클론한뒤   
해당 대시보드를 개방할 포트를 방화벽 설정에서 열어주었고   
백그라운드에서 정상동작이 확인되었습니다.  

### 6. 업데이트 계획   
대시보드의 유용성이 판단되고 사용자가 원한다면,  
해당 데이터는 주기적으로 갱신되는 데이터이기 때문에  
kaggle api를 이용하여 데이터셋을 자동으로 최신화하는 기능을 구현할예정입니다.   

### 7. 유지보수  
서버에서 git pull을 매번 하기는 번거롭기도 하고 서버도 내려야 하는 문제가 있기때문에   
github Actions에 workflow 를 이용하여 서버에 자동으로 배포하는 방법을 채택하였습니다.   


## - :closed_book: 참조한 레퍼런스
[matplotlib](https://matplotlib.org/stable/gallery/units/bar_unit_demo.html#sphx-glr-gallery-units-bar-unit-demo-py),
[plotly](https://plotly.com/python/),
[streamlit](https://docs.streamlit.io/)

## - :closed_book: 외부 리소스 정보
데이터의 출처 : [kaggle](https://www.kaggle.com/datasets/vivovinco/league-of-legends-champion-stats)[^1]

# [👨‍💻 완성된 사이트로 이동합니다.](http://3.38.165.131:8505/)[^1]

[^1]: 사이트로 이동합니다.

<!-- 이부분은 주석이라 표시되지 않습니다. -->


