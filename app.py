
import os
from selenium import webdriver
def Scroll_Page(link):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        driver.get(link)
        html = driver.page_source
    except Exception as e:
        return e
link="https://www.youtube.com/c/Telusko/videos"


if __name__ == "__main__":
    print(Scroll_Page(link))