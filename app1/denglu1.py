from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from app1 import models


from webdriver_manager.chrome import ChromeDriverManager

def login_fr(url, username, password):
    
   
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver.get('http://quanluo.github.io/')

    # 指向驱动位置
    # 下载地址：https://chromedriver.storage.googleapis.com/index.html
    # path = Service('../vent/chromedriver-win64/chromedriver.exe')
    # path = Service('../venv/chromedriver.exe')
    # driver = webdriver.Chrome(service=path)
    # 打开链接
    driver.get(url)
    time.sleep(3)
 
    # 浏览器全屏，可有可无
    driver.maximize_window()
 
    # 找到输入框，这里需要自行在F12的Elements中找输入框的位置，然后在这里写入
    user_input = driver.find_element(by=By.XPATH, value='//input[@type="email"]')
    pw_input = driver.find_element(by=By.XPATH, value='//input[@type="password"]')
    login_btn = driver.find_element(by=By.XPATH, value='//input[@type="submit"]')
    # login_btn = driver.find_element(by=By.CLASS_NAME, value='btn btn-primary')
 
    # 输入用户名和密码，点击登录
    user_input.send_keys(username)
    pw_input.send_keys(password)
    time.sleep(1)
    login_btn.click()
    time.sleep(1)
    
    cookieList=driver.get_cookies()
    
    driver.delete_all_cookies()

    #访问test_url,获取该网站的cookies
    # driver.get(test_url)

    #获取cookies  
    cookie_list = [item["name"] + "=" + item["value"] for item in cookieList]  
    
    cookiestr = ';'.join(item for item in cookie_list)  

    # cookies = {'Cookie':cookiestr}
            
    # requests.get(test_url, cookies=cookies)

    
    print(driver.get_cookies())
    
    row_dengluInfo=models.dengLuInfo.objects.filter(uid=1).first()
    row_dengluInfo.cookie=cookiestr
    row_dengluInfo.save()
 
    return cookiestr

def ss():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://quanluo.github.io/')
    driver.get_screenshot_as_file("123.png")
    driver.quit()
    # driver.close()
    print('ok')


def ss1():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("自动化测试")

if __name__ == '__main__':
    # 定义目标URL信息
    aim_url = {
        'url': 'https://zh.surebet.com/users/sign_in',
        'username': '731772412@qq.com',
        'password': 'dnjsrl0620'
    }
    # 登录
    driver = login_fr(aim_url['url'], aim_url['username'], aim_url['password'])
    
    # ss1()

