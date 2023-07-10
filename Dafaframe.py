import re

import pandas as pd


class PD:
    # 데이터프레임
    _df = None
    # 변수
    _cnt = []  # 순번
    _author = []  # 작성자
    _rink = []  # 링크
    _contents = []  # 내용
    _nml_contents = []
    _hashtags = []  # 해쉬태그
    _likes = []  # 좋아요
    _limit = None
    _date2 = []
    space = []
    _search = 0
    _date = 0
    def reset(self):
        self._df = None
        # 변수
        self._cnt = []  # 순번
        self._author = []  # 작성자
        self._rink = []  # 링크
        self._contents = []  # 내용
        self._nml_contents = []
        self._hashtags = []  # 해쉬태그
        self._likes = []  # 좋아요
        self._limit = None
        self._date2 = []
        self.space = []
        self._search = 0
        self._date = 0

    # 초기화
    def __init__(self):
        print("init")

    def char_filter(self):
        # 공백삭제
        for i in self._contents:
            input_string = re.sub(r'\s{2,}', ' ', i)
            input_string = re.sub(r'[^가-힣a-zA-Z0-9\s]', '', input_string)
            self._nml_contents.append(input_string)

    def counter(self):
        for i in range(1, len(self._df) + 1, 1):
            self._cnt.append(i)

    def author(self):
        self._author = self._df["작성자"]

    def link(self):
        self._rink = self._df["주소"]

    def time(self):
        for i in self._df["작성시간"]:
            date_str = i
            date_part = date_str[:10]
            self._date2.append(date_part)

    def contents(self):
        self._contents = self._df["내용"]

    def tags(self):
        for i in self._df["내용"]:
            tag = re.findall(r'#(\w+)', i)
            self._hashtags.append(tag)

    def likes(self):
        self._likes = self._df["좋아요"]

    def search(self):
        self._search = self._df["검색어"]

    def compatibility(self):

        print("순번:  " + str(len(self._cnt)))
        print("작성자:  " + str(len(self._author)))
        print("주소:  " + str(len(self._rink)))
        print("작성시간:  " + str(len(self._date2)))
        print("내용:  " + str(len(self._contents)))
        print("해쉬:  " + str(len(self._hashtags)))
        print("좋아요:  " + str(len(self._likes)))

    def dateTest(self, df):
        df['작성시간'] = pd.to_datetime(df['작성시간'])
        df = df[df['작성시간'] >= pd.to_datetime(self._limit)]
        return df
    def get(self,df,date):
        self._df = df
        self._limit = date
    def save_csv(self, word):
        self.counter()  # 순서 _cnt
        self.author()  # 작성자 _author
        self.link()  # 링크 _rink
        self.time()  # time _date2
        self.contents()  # 내용 추가하고
        self.char_filter()  # 내용 정규화
        self.tags()  # 해시태그 _hashtags
        self.likes()  # 좋아요 수 _likes
        self.search()  # 검색어 _search
        self.compatibility()

        data = {
            '순번': self._cnt,
            '작성자': self._author,
            '주소': self._rink,
            '작성시간': self._date2,
            '해시태그': self._hashtags,
            '좋아요': self._likes,
            '검색어': self._search,
            '내용': self._nml_contents,
            '보기': ''
        }
        w = pd.DataFrame(data)
        df = self.dateTest(w)
        df.to_csv("C:/Users/USER/Desktop/CSV/" + str(word) + '.csv', index=False, encoding='utf-8-sig')
