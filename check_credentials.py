from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


def check_credentials(username, password):
    
    BASE_URL = "https://edu.enu.kz/"
    NEXT_PAGE = "https://edu.enu.kz/template.html#/welcome"
    
    # Start the browser
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.binary_location = '/usr/bin/google-chrome'
    driver = webdriver.Chrome(options=options, executable_path='/usr/bin/chromedriver')
    
    # Navigate to the website
    driver.get(BASE_URL)
    
    # Fill in the username and password fields
    username_field = driver.find_element(By.ID, 'iin_input')
    password_field = driver.find_element(By.ID, "pass_input")
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    # Click the login button
    login_button = driver.find_element(By.ID, 'Submit1')
    login_button.click()

    # Waiting upload page for get content
    timewait = 5
    print("wait1 for {} seconds....".format(timewait))
    time.sleep(timewait)
    print("check = {}".format(driver.current_url)) 
    result = False
    content = "No"
    # Check if the login was successful
    if NEXT_PAGE in driver.current_url:
        result = True
        driver.get("https://edu.enu.kz/v7/#/schedule/studentView")
        # Wait for the week div to appear
        timewait = 8
        time.sleep(timewait)        
        print("wait2 for {} seconds....".format(timewait))  
        content = driver.page_source
        soup = BeautifulSoup(content, 'html.parser')
        soup = soup.find("div", id="week")
        content = soup.get_text()
    
    driver.quit()
    return result, content
