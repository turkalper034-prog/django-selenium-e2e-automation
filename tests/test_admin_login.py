import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_admin_login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/account/login")
    driver.find_element(By.NAME, "username").send_keys("alper")
    driver.find_element(By.NAME, "password").send_keys("alper7675")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Giriş Başarılı! Tarayıcıda Session Aktif." in driver.page_source
    print("Giriş başarılı")
    time.sleep(5)