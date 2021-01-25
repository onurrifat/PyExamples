from instagramUsersInfo import userName, userPassword
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Instagram:
    def __init__(self, userName, userPassword):
        self.browser = webdriver.Chrome()
        self.userName = userName
        self.userPassword = userPassword
    
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        userNameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        userPassowrdInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        userNameInput.send_keys(self.userName)
        userPassowrdInput.send_keys(self.userPassword)
        userPassowrdInput.send_keys(Keys.ENTER)
        time.sleep(2)


instagram = Instagram(userName,userPassword)
instagram.signIn()









