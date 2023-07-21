import time

from selenium import webdriver
import func


def main2(order):
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com")
    driver.implicitly_wait(5)

    func.login(driver, order[0], order[1])

    driver.implicitly_wait(4)

    url = func.insta_search(order[2])

    driver.get(url)
    driver.implicitly_wait(12)

    fetch = None

    func.select_first(driver)

    result = []
    start = order[4]
    time.sleep(3)

    for i in range(0, int(order[3]), 1):
        try:
            data = func.get_content(driver, order[2])

            if data[2][:20] == fetch:
                break
            else:
                driver.implicitly_wait(5)
                print("게시글 %s 번째  수집 제목: %s , 게시글 날짜: %s " % (i + 1, data[2][:20], data[3][:10]))
                result.append(data)
                time.sleep(3)
                func.move_next(driver)
                fetch = data[2][:20]
        except:
            pass

    return result, start
