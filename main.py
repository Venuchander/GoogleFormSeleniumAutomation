from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


web = webdriver.Chrome()
web.get("Your Google Form link")

time.sleep(2)

name = "Venuchander"
first = web.find_element(By.XPATH,'xpath')
first.send_keys(name)
time.sleep(1)

c_number = "Ph.No"
number = web.find_element(By.XPATH,'xpath')
number.send_keys(c_number)
time.sleep(1)

email = "yourname@gmail.com"
mail = web.find_element(By.XPATH,'xpath')
mail.send_keys(email)

address = "Address"
add_address = web.find_element(By.XPATH,'xpath')
add_address.send_keys(address)

pincode = "000000"
add_pincode = web.find_element(By.XPATH,'xpath')
add_pincode.send_keys(pincode)


dob = "424325"
add_dob = web.find_element(By.XPATH,'xpath')
add_dob.send_keys(dob)

gender = "Male"
add_gender = web.find_element(By.XPATH,'xpath')
add_gender.send_keys(gender)

verification_code = "Random Code"
add_verification_code = web.find_element(By.XPATH,'xpath')
add_verification_code.send_keys(verification_code)

submit = web.find_element(By.XPATH,'xpath')
submit.click()

time.sleep(10)