from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# 配置ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 设置ChromeDriver路径
chrome_driver_path = r'D:\Download\chromedriver-win64\chromedriver.exe'  # 请替换为你的ChromeDriver路径
service = Service(chrome_driver_path)

# 启动浏览器
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 打开一个空白页面
    driver.get("https://skin.mualliance.ltd")

    # 设置cookie
    cookies = [
        {'name': 'Cookie', 'value': 'locale=zh_CN; XSRF-TOKEN=eyJpdiI6IjI2S0ZWUHZZN1lZR0pBUDluazNvVkE9PSIsInZhbHVlIjoiam9rcVZRQjRXd3hNd3BzSTVsc1lBYlRqak5WRjRpWnl3clJWZDd0MVdVVjVXcys1N2cvR1czejUxclg1RWtEV3dZQ0xjNHFsc2E2em1SRnlrMnZLZnhFUVprYnVHdU5Za1FIWUxzVDNManE3SGV4aGNCZ2NxVXdJY2FoTUxtek4iLCJtYWMiOiIzODFjMWVmMWFmYzMzNDQ4NzRiNzhhMWNlNDIzYTA4OTY1MzVlOWYzOTYxZDVjYTRmMDEwYTJlNDdlY2M5YjA1IiwidGFnIjoiIn0%3D; BS_SESSION=eyJpdiI6IlVibFFYRjRCYkczcjQzL2JaS2xYanc9PSIsInZhbHVlIjoiNUpvVFpIWFhhb2c5S1FwTE53bUxyOXpHbnUvSDBkdWVrK1pncE1GM1c3K1ZPVXBDd29oaVpPMG1QSmVqbE9RZ2RhaFl0bDB2YjNUMWtFR2RRQXBQV2FwZ3IzdWxhYmhTME12QWFxUFdSUVp3bzgzUmMwSG1aZUduVjFXaWJtNUMiLCJtYWMiOiI4YjdiYjVlNmNiODY5ODJlNDExMzE1NTY1ODQxNTQ1MDZlMzRiZDUyNDdkMDk2ZDlmMGZiYjYyNjE0OWE5ZWE4IiwidGFnIjoiIn0%3D'},
    ]

    for cookie in cookies:
        driver.add_cookie(cookie)

    # 重新打开目标页面
    driver.get("https://skin.mualliance.ltd/user")

    # 等待页面加载
    time.sleep(5)

    # 查找签到按钮并点击
    sign_in_button = driver.find_element(By.CLASS_NAME, "btn bg-gradient-primary pl-4 pr-4")
    sign_in_button.click()

    # 等待签到完成
    time.sleep(5)

finally:
    # 关闭浏览器
    driver.quit()