#!/usr/bin/env python
# coding: utf-8

# In[2]:


print(hello)


# In[5]:


hello = '안녕하세요'


# In[6]:


print(hello)


# In[9]:


hello = '다시   한번 안녕하세요'
# 띄어쓰기는 상관 없고, 따옴표 안에 있는 내용은 띄어쓰기 반영


# In[10]:


print(hello)


# In[12]:


# 문자형 데이터
#따옴표 안에 있는 글자는 문자로 인식. 문자형 데이터는 앞뒤로 (작은/큰)따옴표를 써 줘야함. 
artist = "bts"
print(artist)


# In[15]:


#숫자형 데이터
bts_members = 7
print(bts_members)


# In[16]:


# 리스트형 데이터
bts_members = ["정국" , "슈가" , "제이홉", "뷔", "진", "지민", "RM"]
print(bts_members)


# In[18]:


print(bts_members[7])
#파이썬은 0부터 시작


# In[19]:


print(bts_members[6])


# In[21]:


# 리스트 안에는 다양한 종류의 데이터를 넣을 수 있음. 문자, 숫자, 변수 
singers=["bts", 7, bts_members]
print(singers)


# In[22]:


a = 10
b = 5


# In[23]:


# 더하기
s1 = a+b
print(s1)


# In[24]:


# 빼기
s2 = a-b
print(s2)


# In[25]:


# 곱하기
s3 = a*b
print(s3)


# In[26]:


#파이썬만 가능한 문법: 문자형 데이터 더하기
singer1 = 'bts'
singer2 = '아이유'

s1 = singer1 + singer2
print(s1)


# In[27]:


#숫자와 문자를 더하면 에러가 남
members=7
s2=singer1 + members
print(s2)


# In[29]:


members="7"
s2=singer1 + members
print(s2)


# # 큰 제목
# ## 두번째 제목
# ### 세번째 제목
# * 특징 1
# * 특징 2
#     * 중 특징 1
#     * 중 특징 2

# # 반복문

# #반복문

# In[31]:


print(0)
print(1)
print(2)
print(3)
print(4)


# In[32]:


for i in [0,1,2,3,4]:
    print(i)


# In[34]:


#반복문 풀어서 보기
i = 0
print(i)

i = 1
print(i)

i = 2
print(i)


# In[36]:


print(i*2)dd


# In[37]:


# 반복문 학습2
bts_members = ['정국', 'RM', '뷔', '지민', '진', '슈가']
print(bts_members)


# In[38]:


for member in bts_members:
    print(member)


# In[ ]:


# 리스트 원소 추가하기
bts_members = ['정국', 'RM', '뷔', '지민', '진', '슈가', '제이홉']


# In[42]:


#append 함수 사용하기 계속 실행시키면 계속 추가됨. 지우고 싶을 때는 원래 값을 가져와서 덮어 씌우는 방법 밖에 없음.
print(bts_members)
bts_members.append('제이홉')
print(bts_members)


# # 파이썬에서 엑셀처럼 보기

# In[43]:


#기본적인 라이브러리는 아나콘다 설치할 때 같이 설치 됨. 
#여기서는 라이브러리에서 pandas 불러오기.
import pandas as pd 


# In[53]:


# 이름 / 좋아하는 가수 / 이유: 컬럼 가지는 테이블 만들기. 리스트 내에 리스트가 원소로 들어감
data = [
    ['오은지', '오아시스', '멋있음'],
    ['곰돌이', '아이유', '노래를 잘 해서'],
    ['멍멍이', '유재하', '노래가 좋아서'],
    ['냐옹이', '악동뮤지션', '화성을 잘 써서'],
    ['욕돌이', '바비킴', '그냥'],
]
print(data)


# In[54]:


#판다스의 라이브러리에 있는 함수를 쓰겠다는 뜻으로 . 찍음. 함수 대소문자 구분해야
data_df = pd.DataFrame(data)
data_df


# In[56]:


#컬럼 이름 바꾸기
data_df.columns = ['이름', '좋아하는 가수', '이유',]
data_df


# In[57]:


data_df.columns = ['Name', 'Like_singer', 'Reason']
data_df


# # 본격적으로 크롤링 하기

# In[58]:


#크롤링 할 수 있는 라이브러리 가져오기
import requests
from bs4 import BeautifulSoup


# In[61]:


#크롤링 할 사이트 주소 알아보기
url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube'
url


# In[62]:


# 크롤링 할 사이트에서 html 가져오기
html = requests.get(url).text
html


# In[67]:


soup = BeautifulSoup(html, 'html.parser')


# In[69]:


#tr 태그 찾기
# len 함수는 리스트 내에 원소가 몇 개(length)인지 확인하는 숫자
list = soup.select('tr')
len(list)


# In[70]:


lst = soup.select('tbody>tr')
len(lst)


# In[71]:


element = lst[0]
element


# In[72]:


category0 = element.select('a')
category0


# In[73]:


category0 = element.select('p>a')
category0


# In[74]:


#한 개 원소를 정확하게 골라오는 작업
category1 = category0[0]
category1


# In[75]:


#원소를 고른 뒤 진짜 원하는 정보만 추출. 태그 사이에 '텍스트' 부분만 가져오기.
category2 = category1.text
category2


# In[76]:


#카테고리 가져오기
category = element.select('p>a')[0].text
category


# In[77]:


#유튜버 이름 가져오기
name0 = element.select('a')
name0


# In[78]:


name0 = element.select('h1>a')
name0


# In[79]:


name1 = name0[0]
name1


# In[80]:


name2 = name1.text
name2


# In[81]:


#탭이나 줄 바꿈 버튼 삭제하기(공백 제거 함수 사용: strip 함수)
name3 = name2.strip()
name3


# In[98]:


name = element.select('h1>a')[0].text.strip()
name


# In[82]:


subs0 = element.select('td')
subs0


# In[85]:


subscriber_cnt = element.select('td.subscriber_cnt')[0].text
subscriber_cnt


# In[86]:


view_cnt = element.select('td.view_cnt')[0].text
view_cnt


# In[90]:


video_cnt = element.select('td.video_cnt')[0].text
video_cnt


# In[93]:


hit = element.select('strong')[0].text
hit


# In[99]:


#리스트로 만들기
element_result = [category, name, subscriber_cnt, view_cnt, video_cnt, hit]
element_result


# In[101]:


# 한 줄 정보 가져오기 
element = lst[0]

#1 카테고리 가져오기 
category = element.select('p > a')[0].text

# 2. 유튜브 이름 가져오기 
name = element.select('h1 > a')[0].text.strip()

# 3. 구독자 수 가져오기 
subscriber_cnt = element.select('td.subscriber_cnt')[0].text

# 4. View 수 가져오기 
view_cnt = element.select('td.view_cnt')[0].text

element_result = [category, name, subscriber_cnt, view_cnt,  video_cnt, hit]
element_result


# In[102]:


# 100번 반복하기
result=[]

for element in lst: 
    
    #1 카테고리 가져오기 
    category = element.select('p > a')[0].text

    # 2. 유튜브 이름 가져오기 
    name = element.select('h1 > a')[0].text.strip()

    # 3. 구독자 수 가져오기 
    subscriber_cnt = element.select('td.subscriber_cnt')[0].text

    # 4. View 수 가져오기 
    view_cnt = element.select('td.view_cnt')[0].text

    element_result = [category, name, subscriber_cnt, view_cnt,  video_cnt, hit]

    result.append(element_result)


# In[103]:


result


# In[104]:


# 표 형태로 만들기
result_df = pd.DataFrame(result)
result_df


# In[105]:


result_df.columns = ['카테고리', '이름', '구독자수', '조회수', '동영상순', '조회수']
result_df


# In[109]:


#엑셀 파일로 저장하기
result_df.to_excel('youtube_top100.xlsx', index = False)

