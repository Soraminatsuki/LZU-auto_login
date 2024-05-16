import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import subprocess
from requests.exceptions import ReadTimeout

# 用户名和密码变量
username = ""
password = ""
# 设置Chrome驱动路径
chrome_driver_paths = r'C:\Program Files\Google\Chrome\Application\chromedriver-win64\chromedriver.exe'  # 替换为实际的chromedriver路径

def check_internet_connection(url="https://www.baidu.com", timeout=1):
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code == 200
    except (requests.ConnectionError, ReadTimeout):
        return False

def kill_chromedriver():
    try:
        # 确保所有chromedriver进程被终止
        subprocess.call(["taskkill", "/F", "/IM", "chromedriver.exe", "/T"], stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Error killing chromedriver: {e}")

def get_current_ssid():
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "interfaces"], text=True, encoding="utf-8")
        for line in result.split("\n"):
            if "SSID" in line:
                return line.split(":")[1].strip()
    except Exception as e:
        print(f"Error getting current SSID: {e}")
    return None

def connect_to_wifi(profile_name):
    try:
        subprocess.call(["netsh", "wlan", "connect", f"name={profile_name}"])
        time.sleep(3)  # 等待连接完成
    except Exception as e:
        print(f"Error connecting to WiFi: {e}")

# 检查是否连接到指定的SSID
current_ssid = get_current_ssid()
if current_ssid != "LZU":
    print(f"当前未连接到LZU WiFi，当前连接的是 {current_ssid}，尝试连接到LZU")
    connect_to_wifi("LZU")

# 再次检查是否已经连接到LZU WiFi
current_ssid = get_current_ssid()
if current_ssid != "LZU":
    print("无法连接到LZU WiFi，请检查网络设置。")
else:
    print("已经连接到LZU WiFi，继续执行后续代码")

    # 检查是否有网络连接
    if check_internet_connection():
        print("已经连接到互联网")
    else:
        print("没有网络连接，尝试登录校园网")

        # 配置Chrome选项
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # 无头模式，不显示浏览器界面
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")

        # 设置Chrome驱动路径
        chrome_driver_path = chrome_driver_paths

        # 创建浏览器驱动
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        try:
            # 打开校园网登录页面
            driver.get("http://10.10.0.166/")

            # 设置窗口大小
            driver.set_window_size(868, 1020)

            # 等待页面加载
            time.sleep(2)

            # 点击第二个标签
            tab_item = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".tab-item:nth-child(2)"))
            )
            tab_item.click()

            # 点击并选择域选项
            domain_dropdown = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "domain"))
            )
            domain_dropdown.click()

            domain_option = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//option[. = '@eLearning']"))
            )
            domain_option.click()

            # 输入账号
            username_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.click()
            username_field.send_keys(username)

            # 输入密码
            password_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "password"))
            )
            password_field.click()
            password_field.send_keys(password)

            # 点击登录按钮
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "login"))
            )
            login_button.click()

            # 等待登录完成
            time.sleep(1)

            # 使用 check_internet_connection 函数来验证是否成功连接到互联网
            if check_internet_connection():
                print("登录成功并连接到互联网")
            else:
                print("登录失败或未连接到互联网")

        finally:
            # 关闭浏览器
            driver.quit()
            # 确保所有chromedriver进程被终止
            kill_chromedriver()
