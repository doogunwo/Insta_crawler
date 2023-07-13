from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def login(driver, id, pw):
    while (1):
        try:
            # ID
            _id = driver.find_element(By.NAME, "username").send_keys(id)
            # PW
            _pw = driver.find_element(By.NAME, "password").send_keys(pw)
            # 로그인 성공
            driver.find_element(By.XPATH, "//button[@type='submit']").click()

            driver.implicitly_wait(10)

            btn_later2 = driver.find_element(By.CLASS_NAME, '_a9--._a9_1')
            btn_later2.click()
            break

        except:
            print("로그인 실패")
            break


def get_content(driver, search):

    date2 = driver.find_element(By.CLASS_NAME, "_aaqe")
    date = date2.get_attribute('datetime')
    # 링크
    link = driver.current_url
    # 작성자
    author = driver.find_element(By.CLASS_NAME, '_aaqt').text
    # 본문 내용
    #
    content = driver.find_element(By.CSS_SELECTOR, '_a9zm').text
    # 시간
    # date= driver.find_element(By.CSS_SELECTOR,'time._aaqe').text

    # 좋아요
    try:
        like = driver.find_element(By.CLASS_NAME, '_ae5m').text
    except:
        like = 0

    data = [link, author, content, date, like, search]

    return data

def rimit(driver):
    dd = driver.find_element(By.CLASS_NAME, "_ac2a").text
    return dd
def move_next(driver):  # 다음 게시글 조회

    right = driver.find_element(By.CLASS_NAME, "_abl-")
    right.click()
    driver.implicitly_wait(4)


def select_first(driver):
    fir = driver.find_element(By.CLASS_NAME, '_aagw').click()
    print(fir)
    driver.implicitly_wait(10)


def insta_search(word):
    url = 'https://www.instagram.com/explore/tags/' + word + "/"
    return url
