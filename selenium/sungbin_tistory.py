from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google_search():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # 이 줄이 있으면 화면 안 보임
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.maximize_window()
    driver.get("https://sungbin-park.tistory.com/")
    
    # search_box = driver.find_element(By.NAME, "q")
    # search_box.send_keys("sungbin tistory page")
    # search_box.submit()
    
    time.sleep(6)  # 결과 확인을 위한 시간
    assert "QA Test" in driver.title
    driver.quit()
