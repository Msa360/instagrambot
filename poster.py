
# imports
import os
import random
from bot import Bot
from dotenv import load_dotenv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# set up
load_dotenv()
user_name = os.getenv("USERNAME")
pwd = os.getenv("PASSWORD")

# start instance of bot
bot = Bot()
bot.login(username=user_name, password=pwd)

# bot.create_post(media="bestfastfoodclips/test.jpg", description="hello this is a test")
# time.sleep(30)
    

def select_rand_post():
    account = random.choice(os.listdir('rawscraped'))
    file = random.choice(os.listdir('rawscraped/' + account))
    file_path = "rawscraped/" + account + "/" + file
    return file_path

def manual_post():
    account = random.choice(os.listdir('rawscraped'))
    file = random.choice(os.listdir('rawscraped/' + account))
    file_path = "rawscraped/" + account + "/" + file
    bot.create_post(media=file_path, description="Tag a friend who would like this!  --credits: @" + account)
    
manual_post()

