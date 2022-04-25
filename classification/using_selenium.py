import time
from selenium import webdriver
from selenium.common.exceptions import InvalidCookieDomainException
from webdriver_manager.chrome import ChromeDriverManager
import pickle
import json
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from scrapy import Selector
from selenium.webdriver.chrome.options import Options
from classification.location_finder import locate_text

s = Service(ChromeDriverManager().install())

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--enable-javascript")
chrome_options.headless = True

# driver = webdriver.Chrome(options=chrome_options, service=s)
#
# driver.get('https://images.google.com/')
# cookies = pickle.load(open("classification/cookies.pkl", "rb"))
# for cookie in cookies:
#     try:
#         driver.add_cookie(cookie)
#     except InvalidCookieDomainException:
#         continue


def use_sel_model(img_param):
    try:
        driver = webdriver.Chrome(options=chrome_options, service=s)

        driver.get('https://images.google.com/')
        cookies = pickle.load(open("classification/cookies.pkl", "rb"))
        for cookie in cookies:
            try:
                driver.add_cookie(cookie)
            except InvalidCookieDomainException:
                continue

        # img_param = r'C:/Users/pixarsart/StampBox Classification/stampbox' + img_param
        # driver.add_cookie({'domain': '.google.com', 'expiry': 1653048163, 'httpOnly': False, 'name': '1P_JAR', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '2022-04-20-12'})
        try:
            driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Search by image"]').click()
        except Exception as e:
            driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Bildersuche"]').click()
        driver.find_element(By.CSS_SELECTOR, 'a[href="about:invalid#zClosurez"]').click()
        driver.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(img_param)
        response = Selector(text=driver.page_source)
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
        first_text = response.css('a[style="font-style:italic"] ::text').get('')
        print(first_text)
        f_text = locate_text(first_text, flag=True)
        if f_text:
            print('if f_text', f_text)
            return f_text
        else:
            print('else f_text')
            text = ' '.join(response.css('#rcnt ::text').getall())
            if text:
                text = locate_text(text)
                return text
            else:
                return None
    except Exception as e:
        print('[METHOD: POST] [USING SELENIUM] caught exception, ', e)
        return None


if __name__ == '__main__':
    image_path = r"C:\Users\pixarsart\PycharmProjects\StampBox Classifications\Images\Stamps_images\Untitled design (15).png"
    use_sel_model(image_path)
