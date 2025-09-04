from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# 환경변수에서 민감정보 로딩
EMAIL = os.getenv("VIDEOSTEW_EMAIL")
PASSWORD = os.getenv("VIDEOSTEW_PASS")

driver = webdriver.Chrome()
driver.get("https://videostew.com/login")

wait = WebDriverWait(driver, 10)

# 이메일 입력
email_input = wait.until(EC.element_to_be_clickable((By.NAME, "email")))
email_input.click()
email_input.clear()
email_input.send_keys(EMAIL)

# 비밀번호 입력
pass_input = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
pass_input.click()
pass_input.clear()
pass_input.send_keys(PASSWORD)

# 로그인 버튼 클릭
login_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and text()="Login"]')))
login_btn.click()

# 로그인 성공 여부 확인 (예: 대시보드 URL 또는 특정 요소 존재)
dashboard = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".dashboard")))
print("✅ 로그인 성공!")
