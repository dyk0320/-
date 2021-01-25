from utils import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import json

chrome_options = webdriver.ChromeOptions()

prefs = {"profile.managed_default_content_settings.images": 2}

chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(Chromedriver_path)
driver.get('https://portal.pku.edu.cn/portal2017/login.jsp')

#selenium_click(driver, '//*[@id="ng-app"]/div[1]/header/section/section[1]/section[1]/ul[1]')

usernames = selenium_wait_xpaths(driver, '//*[@id="user_name"]')
usernames[0].send_keys("username")
passwords = selenium_wait_xpaths(driver, '//*[@id="password"]')
passwords[0].send_keys("password")

time.sleep(1)

selenium_click(driver, '//*[@id="logon_button"]')
selenium_click(driver, '//*[@id="epidemic"]')
time.sleep(5)
windows = driver.window_handles
driver.switch_to.window(windows[1])

#当日是否留在宿舍
selenium_click(driver, '//*[@id="pane-daily_info_tab"]/form/div[9]/div/label[1]')

#体温
# tempMinus = random.randint(1, 4)
# i = 1
# while i <= tempMinus:
#     selenium_click(driver, '//*[@id="pane-daily_info_tab"]/form/div[12]/div/div/span[1]/i')
#     i += 1

#症状选择
#radioChecks = selenium_wait_xpaths(driver, '//*[@id="pane-daily_info_tab"]/form/div[13]/div/label[2]/span[1]/input')
#radioChecks[0].send_keys(Keys.SPACE)

#是否存在以下症状
selenium_click(driver, '//*[@id="pane-daily_info_tab"]/form/div[14]/div/label[2]')

#疫情诊断
#selenium_click(driver, '//*[@id="pane-daily_info_tab"]/form/div[14]/div/div/div/span')
#selenium_click(driver, '/html/body/div[2]/div[1]/div[1]/ul/li[1]/span')

selenium_click(driver, '//*[@id="pane-daily_info_tab"]/form/div[15]/div/div/div[1]/span')
selenium_click(driver, '/html/body/div[2]/div[1]/div[1]/ul/li[1]/span')


#是否出校
selenium_click(driver, '//*[@id="pane-daily_info_tab"]/form/div[16]/div/label[2]/span[1]')

selenium_click(driver, '//*[@id="pane-daily_info_tab"]/form/div[18]/div/button')
driver.quit()


