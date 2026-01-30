import undetected_chromedriver as uc
import time

driver = uc.Chrome(version_main=144)
driver.get("https://www.hikeamr.org")


time.sleep(3)

driver.save_screenshot("image.png")