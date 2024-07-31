import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# @pytest.mark.smoke

#def test_select_product():
driver = webdriver.Chrome()

driver.get("http://52.168.145.209:3000/")
driver.maximize_window()
print(driver.title)
print(driver.session_id)
assert driver.title == "Lp Soul Store"
time.sleep(2)

driver.find_element(By.XPATH,"//a[normalize-space()='T-SHIRTS']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div//div[1]//section[1]//a[1]//div[1]//div[1]//img[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[normalize-space()='Customize it']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[@class='product-customizer']//div[4]//p[1]//*[name()='svg']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//body//div//img[4]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[normalize-space()='back']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//body//div//img[2]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[normalize-space()='Preview']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[normalize-space()='Add To Cart']").click()
time.sleep(3)
driver.find_element(By.XPATH, "(//*[name()='svg'][@class='bi bi-cart '])[1]").click()
time.sleep(10)
#driver.get("https://dev-6o0dtt0tzs4774yn.us.auth0.com/u/login?state=hKFo2SBKUUhpcEdMakRPeks5U2s4LXlnLXYwMGgxbVdBd1RJUqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIDE3dUFPMDF3YWNIbFlnSEZzZFRfeGl3eVk3dlVZZzZro2NpZNkgS2tHM0F2OWtKMWh4dndod2lyZERROUJVaTlIeXpRWTQ")
#driver.find_element(By.XPATH,"(//input[@id='username'])[1]").send_keys("ranveer.s@lpcloudlab.com")
#time.sleep(2)
#driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Lpcloud@123?")
#time.sleep(2)
#driver.find_element(By.XPATH,"//button[normalize-space()='Continue']").click()
#time.sleep(2)
driver.close()
