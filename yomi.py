
# imports

import os
from dotenv import load_dotenv
from instapy_cli import client
from selenium import webdriver
from instascrape import *
import time


load_dotenv()

# universal var
user_name = os.getenv("USERNAME")
pwd = os.getenv("PASSWORD")


class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome('/Users/arnaudtremblay/Downloads/chromedriver')


    def __home(self):    
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)

    def __is_logged(self):
        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        except:
            return True
        else:
            return False

    def __hp_is_notif(self):
        try:
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
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
            username_input = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
            username_input.send_keys(username)
            password_input = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
            password_input.send_keys(password)
            submit = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
            submit.click()
            print("trying to connect...")
            time.sleep(2)
            if (self.__hp_is_notif()):
                hp_notif = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
                hp_notif.click()
                time.sleep(3)
            print("Successfully connected")
    

    def create_post(self):
        np_btn = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button")
        np_btn.click()
        time.sleep(2)
        browse_btn = self.driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/form/input")
        browse_btn.send_keys("/Users/arnaudtremblay/PycharmProjects/igbot/other/Unknown.jpeg")
        
        time.sleep(2)

        print("Successfully created post!")

    



def main():
    bot = Bot()
    bot.login(username=user_name, password=pwd)
    bot.create_post()
    time.sleep(30)
    
    
    
    


if __name__ == "__main__":
    main()