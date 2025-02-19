import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import sys
import os

# 设置默认编码为utf-8
sys.stdout.reconfigure(encoding='utf-8')

# 设置Chrome选项
options = uc.ChromeOptions()
options.headless = True  # 设置为无头模式

# 启动浏览器
driver = uc.Chrome(options=options, version_main=133)  # 指定ChromeDriver主版本号

try:
    # 打开目标页面
    driver.get("https://skin.mualliance.ltd/user")

    # 等待页面加载
    time.sleep(5)

    # 从环境变量读取cookie
    cookie_string = os.getenv('COOKIE')
    if not cookie_string:
        print("环境变量 'COOKIE' 未设置")
        sys.exit(1)

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
    wait = WebDriverWait(driver, 10)  # 设置等待时间为10秒
    try:
        sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.bg-gradient-primary.pl-4.pr-4")))

        # 检查按钮是否可点击
        if sign_in_button.is_enabled():
            sign_in_button.click()
            print("签到按钮已点击")
        else:
            print("签到按钮不可点击")
    except TimeoutException:
        print("已经签到或按钮不可用")
    finally:
        driver.quit()

finally:
    # 关闭浏览器并忽略OSError异常
    try:
        driver.quit()
    except OSError:
        pass