import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# 设置默认编码为utf-8
sys.stdout.reconfigure(encoding='utf-8')

# 启动浏览器
driver = uc.Chrome()

try:
    # 打开目标页面
    driver.get("https://skin.mualliance.ltd/user")

    # 等待页面加载
    time.sleep(5)

    # 设置cookie
    cookies = [
        {'name': 'locale', 'value': 'zh_CN'},
        {'name': 'XSRF-TOKEN', 'value': 'eypdiI6IjIS0ZWUHZZN1lZR0pBUDluazNvVkE9PSInZHVlIjoiam9rcVZRQjRXd3hNd3BzSTVsc1lBYlRqak5WRjRpWnl3clJWZDd0MVdVVjVXcys1N2cvR1czejUxclg1RWtEV3dZQ0xjNHFsc2E2em1SRnlrMnZLZnhFUVprYnVHdU5Za1FIWUxzVDNManE3SGV4aGNCZ2NxVXdJY2FoTUxtek4iLCJtYWMiOiIzODFjMWVmMWFmYzMzNDQ4NzRiNzhhMWNlNDIzYTA4OTY1MzVlOWYzOTYxZDVjYTRmMDEwYTJlNDdlY2M5YjA1IiwidGFnIjoiIn0%3D'},
        {'name': 'BS_SESSION', 'value': 'eyJpdiI6IlVibFFYRjRCYkczcjQzL2JaS2xYanc9PSIsInZhbHVlIjoiNUpvVFpIWFhhb2c5S1FwTE53bUxyOXpHbnUvSDBkdWVrK1pncE1GM1c3K1ZPVXBDd29oaVpPMG1QSmVqbE9RZ2RhaFl0bDB2YjNUMWtFR2RRQXBQV2FwZ3IzdWxhYmhTME12QWFxUFdSUVp3bzgzUmMwSG1aZUduVjFXaWJtNUMiLCJtYWMiOiI4YjdiYjVlNmNiODY5ODJlNDExMzE1NTY1ODQxNTQ1MDZlMzRiZDUyNDdkMDk2ZDlmMGZiYjYyNjE0OWE5ZWE4IiwidGFnIjoiIn0%3D'},
    ]

    for cookie in cookies:
        driver.add_cookie(cookie)

    # 重新打开目标页面
    driver.get("https://skin.mualliance.ltd/user")

    # 等待页面加载
    time.sleep(5)

    # 使用显式等待查找签到按钮并检查是否可点击
    wait = WebDriverWait(driver, 20)
    sign_in_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.bg-gradient-primary.pl-4.pr-4")))

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