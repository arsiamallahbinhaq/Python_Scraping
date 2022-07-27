from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\ACER\Downloads\chromedriver.exe")
driver.get('https://id.carousell.com/categories/photography-6/?searchId=-6cWpD')

# #root > div > div.D_G > div > div.D_Q > main > div > div > div:nth-child(1) > div > div.D_AX > a:nth-child(2) > p.D_lf.D_kW.D_lg.D_lj.D_lm.D_lp.D_lr.D_ln.D_lb

judul = driver.find_element(By.CSS_SELECTOR, 'main > div > div > div:nth-child(1) > div > div.D_AX > a:nth-child(2) > p').text
print(judul)

driver.quit()