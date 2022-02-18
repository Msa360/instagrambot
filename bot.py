
# imports

import os

from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

import time


load_dotenv()

# universal var
user_name = os.getenv("USERNAME")
pwd = os.getenv("PASSWORD")


class Bot():

    def __init__(self):
        self.driver = webdriver.Chrome('/Users/arnaudtremblay/Downloads/chromedriver')
        self.driver.implicitly_wait(20)

    def __home(self):    
        self.driver.get("https://www.instagram.com/")

    def __is_logged(self):
        try:
            self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        except:
            return True
        else:
            return False


    def __hp_is_notif(self):
        try:
            self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")
        except:
            return False
        else:
            return True


    def login(self, username, password):
        self.__home()
        self.username = username
        self.password = password
        if (self.__is_logged()):
            pass # coming soon a system for deconnecting active user to reconnect new user
        else:
            username_input = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
            username_input.send_keys(username)
            password_input = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
            password_input.send_keys(password)
            submit = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
            submit.click()
            print("trying to login...")
            if (self.__hp_is_notif()):
                hp_notif = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")
                hp_notif.click()
            print("Successfully logged in")
    

    def create_post(self, media, description):
        # new post button
        np_btn = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button")
        np_btn.click()
        

        # browse media and send it to ig
        browse_btn = self.driver.find_element(By.XPATH, "/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/form/input")
        browse_btn.send_keys("/Users/arnaudtremblay/PycharmProjects/igbot/" + media)
        

        # button "continue" while posting
        con_btn = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button")
        con_btn.click()
        

        # button "continue" number 2 while posting
        con_btn2 = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button")
        con_btn2.click()
       

        # photo settings -- description
        desc = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea")
        desc.send_keys(description)

        # button "share"
        share_btn = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button")
        share_btn.click()
        time.sleep(15)
        print("Successfully created post with: " + media + " \"" + description + "\"")

        # close "post succesfully created" popup
        cp_btn = self.driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/button")
        cp_btn.click()
        


    


