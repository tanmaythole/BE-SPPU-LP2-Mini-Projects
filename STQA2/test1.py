from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()  
driver.get("http://localhost/PHP-Discussion-Forum/")

driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/button[1]').click()
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="username"]').send_keys("admin")
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("admin25")
driver.find_element(By.XPATH, '//*[@id="loginModal"]/div/div/div[2]/form/button').click()
time.sleep(2)

ele = driver.find_element(By.LINK_TEXT, 'Read More')
driver.execute_script("arguments[0].click()", ele)
time.sleep(2)

try:
    driver.find_element(By.NAME, 'title').send_keys("Question Title Testing")
    driver.find_element(By.NAME, 'desc').send_keys("Question Description Testing")
    driver.find_element(By.XPATH, '/html/body/div[4]/form/button').click()
    time.sleep(2)
except:
    print("Login Required")

ele = driver.find_element(By.XPATH, '//*[@id="space"]/div/div/h5/a')
driver.execute_script("arguments[0].click()", ele)
time.sleep(2)

try:
    driver.find_element(By.NAME, 'comment').send_keys("Comment Testing")
    driver.find_element(By.XPATH, '/html/body/div[4]/form/button').click()
    time.sleep(2)
except:
    print("Login Required")

try:
    ele = driver.find_element(By.XPATH, '//*[@id="navbarDropdown"]')
    driver.execute_script("arguments[0].click()", ele)
    time.sleep(2)
    logout = driver.find_element(By.XPATH, '//*[@id="navbarSupportedContent"]/div/ul/li[2]/a')
    driver.execute_script("arguments[0].click()", logout)
    time.sleep(2)
except:
    print()


print("\n\nForum Tested Successfully")

driver.close()