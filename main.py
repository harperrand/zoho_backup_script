# Python imports
import getpass

# Selenium imports
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# DOMAIN should match the url used when you visit https://accounts.zoho.com, accounts.zoho.eu, etc
DOMAIN = ".com"

# Enter info needed for Selenium to access Zoho
un = input("Please enter your Zoho username: ")
pw = getpass.getpass("Please enter your Zoho password: ")
org_id = input("Please enter your Zoho Org ID: ")
backup_id = input("Please enter the Zoho Backup ID: ")
attachments = int(input("Please enter the number of attachments in the backup: "))

# Start a new Selenium webdriver
driver = webdriver.Chrome()

# Log in to Zoho
driver.get(f"https://accounts.zoho.{DOMAIN}/signin")
username = driver.find_element(By.ID, "login_id")
username.send_keys(un)
button = driver.find_element(By.ID, "nextbtn")
button.click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'password')))
password = driver.find_element(By.ID, "password")
password.send_keys(pw)
button.click()

# Once we are logged in, navigate to the URLs with the backup files
WebDriverWait(driver, 20).until(EC.url_matches(f"https://accounts.zoho.{DOMAIN}/home#profile/personal"))
driver.get(f"https://download-accl.zoho.{DOMAIN}/v2/crm/{org_id}/backup/{backup_id}/Data_001.zip")
for i in range(1, attachments + 1):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.COMMAND + 't')
    if i < 10:
        driver.get(f"https://download-accl.zoho.{DOMAIN}/v2/crm/{org_id}/backup/{backup_id}/Attachments_00{i}.zip")
    elif i < 100:
        driver.get(f"https://download-accl.zoho.{DOMAIN}/v2/crm/{org_id}/backup/{backup_id}/Attachments_0{i}.zip")
    else:
        driver.get(f"https://download-accl.zoho.{DOMAIN}/v2/crm/{org_id}/backup/{backup_id}/Attachments_{i}.zip")