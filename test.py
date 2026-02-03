import undetected_chromedriver as uc
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# Login Info:
# MusicHater
username = "MusicHater"
# 1AmABot
password = "1AmABot"

driver = uc.Chrome(version_main=144)
driver.get("https://www.hikeamr.org")
login_obj = driver.find_element(By.XPATH, "//div[@id='masterPageUC_MSTR51']//div[@id='navbarSupportedContent']//div[@class='right-menu']//ul/li[@id='ulMenuItem_100031']/a")
print(str(login_obj.text))

login_obj.click()

print(driver.current_url)

username_obj = driver.find_element(By.XPATH, "//div[@class='login-inputs']//div[@id='un_box']/input")
password_obj = driver.find_element(By.XPATH, "//div[@class='login-inputs']//div[@id='pw_box']/input")

username_obj.send_keys(username)
password_obj.send_keys(password)

print(username_obj.text)
print(password_obj.text)

form_obj = driver.find_element(By.XPATH, "//div[@class='login-inputs_link']/input[@id='btnSecureLogin']")
print("Button text:")
print(form_obj.get_attribute("title"))
form_obj.click()

time.sleep(5)

driver.save_screenshot("image.png")


# driver.quit()