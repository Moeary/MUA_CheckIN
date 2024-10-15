import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import os

# 设置默认编码为utf-8
sys.stdout.reconfigure(encoding='utf-8')

# 启动浏览器
driver = uc.Chrome()

try:
    # 打开目标页面
    driver.get("https://skin.mualliance.ltd/user")

    # 等待页面加载
    time.sleep(5)

    # 从环境变量读取cookie
    cookie_string = os.getenv('COOKIE')
    cookies = []
    for cookie in cookie_string.split('; '):
        name, value = cookie.split('=', 1)
        cookies.append({'name': name, 'value': value})

    # 设置cookie
    for cookie in cookies:
        driver.add_cookie(cookie)

    # 重新打开目标页面
    driver.get("https://skin.mualliance.ltd/user")

    # 等待页面加载
    time.sleep(5)

    # 使用显式等待查找签到按钮并检查是否可点击
    wait = WebDriverWait(driver, 20)
    sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.bg-gradient-primary.pl-4.pr-4")))

    # 检查按钮是否可点击
    if sign_in_button.is_enabled():
        sign_in_button.click()
        print("签到按钮已点击")
    else:
        print("签到按钮不可点击")

    # 等待签到完成
    time.sleep(5)

finally:
    # 关闭浏览器并忽略OSError异常
    try:
        driver.quit()
    except OSError:
        pass