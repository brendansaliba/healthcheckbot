from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time

# UNCOMMENT AND SET YOUR ASU USERNAME AND PASSWORD
# username =
# password =


## CREATE WEBDRIVER
driver = webdriver.Chrome(ChromeDriverManager().install())
PATH = "chromedriver.exe"
GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = GOOGLE_CHROME_PATH


## SUBMIT HEALTHCECKS

# login and wait for 5 seconds to ensure login success.
driver.get("https://weblogin.asu.edu/cas/login?service=https%3A%2F%2Fweblogin.asu.edu%2Fcgi-bin%2Fcas-login%3Fcallapp%3Dhttps%253A%252F%252Fweblogin.asu.edu%252Fserviceauth%252Foauth2%252Fnative%252Fallow%253Finit%253Dfalse%2526response_type%253Dcode%2526client_id%253Dhealthcheck-web%2526redirect_uri%253Dhttps%25253A%25252F%25252Fwww.asu.edu%25252Fhealthcheck%25252Fpreferences.html%2526state%253DuFT6XqdWYxj1JWJL2n4x3k-q4Do3gcuws6WMOq.diAIvLfxW6JvbPTwFO61mNiJa%2526code_challenge_method%253DS256%2526code_challenge%253DJT79b5WhTEvJ-SnolhiXsBZBK-BF9h4KnH8jUNn_vy8%2526scope%253Dhttps%25253A%25252F%25252Fapp.m.asu.edu%25252Fhealthcheck")
print(driver.title)
driver.maximize_window()
username_in = driver.find_element_by_name("username")
password_in = driver.find_element_by_name("password")

username_in.send_keys(username)
password_in.send_keys(password)
password_in.send_keys(Keys.RETURN)
time.sleep(5)

# pull up the healthcheck submission
driver.get("https://dailycheck.m.asu.edu/")
time.sleep(2)
print(driver.title)

# try and click the buttons, if this does not work something is wrong or a healthceck has been submitted already
try:
    none_button = driver.find_element_by_xpath('//button/span[text()="None"]')
    none_button.click()
    print("Health check not submitted. Submitting now.")
    time.sleep(2)
    next_button = driver.find_element_by_xpath('//button/span[text()="Next"]')
    next_button.click()
    time.sleep(2)

    none_button_2 = driver.find_element_by_xpath('//button/span[text()="None"]')
    none_button_2.click()
    time.sleep(2)

    submit_button = driver.find_element_by_xpath('//button/span[text()="Submit"]')
    submit_button.click()

    print("Health check submitted for {}".format(username))
except:
    print("Something went wrong submitting for {}. Either a health check has already be submitted or there was a problem submitting.".format(brendan_username))

driver.get("https://weblogin.asu.edu/cas/logout?eventSource=healthcheck-web")
print("{} logged out".format(password))
