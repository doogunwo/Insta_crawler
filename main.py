import argparse
import pandas as pd
import Dafaframe
import insta
import math
import time

def parser_to_word():
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', type=str, default="1", help="input id")
    parser.add_argument('--pw', type=str, default="1", help="input pw")
    parser.add_argument('--w', type=str, default="dd.txt", help="word or text.path")
    parser.add_argument('--n', type=int, default=100, help="number of post")
    parser.add_argument('--l', type=str, default="2023-01-01", help="limit date")
    args = parser.parse_args()
    word1 = [args.id, args.pw, args.w, args.n, args.l]
    txt= args.w
    if txt.lower().endswith('.txt'):
        with open(txt, 'r') as file:
            file_content = file.read()
            file_content = file_content.split("\n")
            word1[2] = file_content
    else:
        word1[2] = txt

    return word1

def parser_to_word2():

        print("아이디 패스워드 검색어 갯수 제한날짜 를 차례대로 입력해주세요.")# 1 3 5 7
        word = input("명령어를 입력해주세요 >>")
        word1 = word.split(" ")

        return word1

def main_word(order):
    start_time = time.time()
    math.factorial(100000)
    res, start = insta.main2(order)
    df = pd.DataFrame(res, columns=['주소', '작성자', '내용', '작성시간', '좋아요', '검색어'])
    obj = Dafaframe.PD()
    obj.get(df, order[4])
    obj.save_csv(order[2])

    end = time.time()
    timing = end - start_time
    print("크롤링시간은 %s 초 입니다." % (str(timing)))

def main_list(order):
    try:
        start_time = time.time()
        math.factorial(100000)
        list3 = order[2]
        obj = Dafaframe.PD()
        for i in list3:
            try:
                order[2] = i
                res, start = insta.main2(order)
                df = pd.DataFrame(res, columns=['주소', '작성자', '내용', '작성시간', '좋아요', '검색어'])
                obj.get(df, order[4])
                obj.save_csv(order[2])
                obj.reset()
            except:
                pass

        end = time.time()
        timing = end - start_time
        print("크롤링시간은 %s 초 입니다." % (str(timing)))
    except:
        pass
if __name__ == "__main__":
    order = parser_to_word()
    if isinstance(order[2],str):
        main_word(order)

    elif isinstance(order[2],list):
        main_list(order)
