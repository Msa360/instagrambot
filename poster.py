
# imports
import os
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

bot.create_post(media="bestfastfoodclips/test.jpg", description="hello this is a test")
time.sleep(30)
    
    
    
    


