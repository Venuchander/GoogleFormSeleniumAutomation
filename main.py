from selenium import webdriver
import time
from selenium.webdriver.common.by import By


web = webdriver.Chrome()
web.get("Google Form Link")

time.sleep(2)

name = "Name"
first = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
first.send_keys(name)
time.sleep(1)

c_number = "8807789175"
number = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
number.send_keys(c_number)
time.sleep(1)

email = "venuchander1@gmail.com"
mail = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
mail.send_keys(email)

address = "NO 37A, Velan Nagar 5th Street, Valasaravakkam, Chennai 87"
add_address = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
add_address.send_keys(address)

pincode = "600087"
add_pincode = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
add_pincode.send_keys(pincode)


dob = "07032006"
add_dob = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
add_dob.send_keys(dob)

gender = "Male"
add_gender = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
add_gender.send_keys(gender)

verification_code = "GNFPYC"
add_verification_code = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
add_verification_code.send_keys(verification_code)

submit = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
submit.click()

time.sleep(10)
